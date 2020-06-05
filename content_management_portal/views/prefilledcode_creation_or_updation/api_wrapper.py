import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal. \
    interactors.prefilledcode_create_or_update_interactor \
        import PrefilledCodeCreateOrUpdateInteractor

from content_management_portal.storages.prefilledcode_storage_implementation import \
    PrefilledCodeStorageImplementation
from content_management_portal.presenters.prefilledcode_presenter_implementation import \
    PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id=kwargs['question_id']

    requested_data = kwargs['request_data']

    storage = PrefilledCodeStorageImplementation()
    presenter = PresenterImplementation()

    interactor = PrefilledCodeCreateOrUpdateInteractor(
                        storage=storage,presenter=presenter)

    requested_data = requested_data["prefilledcode_details"]

    response = interactor.prefilledcode_create_or_update( \
                    question_id=question_id, \
                        question_prefilledcode_list=requested_data)

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)

