import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.hint_create_or_update_interactor \
    import HintCreateOrUpdateInteractor
from content_management_portal.presenters.hint_presenter_implementation \
    import PresenterImplementation
from content_management_portal.storages.hint_storage_implementation import \
    HintStorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs["question_id"]
    request_data = kwargs["request_data"]
    hint_details = request_data["hint_details"]

    storage = HintStorageImplementation()
    presenter = PresenterImplementation()

    interactor = HintCreateOrUpdateInteractor(storage=storage, presenter=presenter)

    response = interactor.hint_create_or_update(question_id=question_id, \
                                hint_details=hint_details)

    json_data = json.dumps(response)
    return HttpResponse(json_data, status=201)
