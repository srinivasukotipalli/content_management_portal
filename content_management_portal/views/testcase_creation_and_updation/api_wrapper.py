import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.interactors.testcase_create_or_update_interactor \
    import CaseCreateOrUpdateInteractor
from content_management_portal.presenters.testcase_presenter_implementation \
    import PresenterImplementation
from content_management_portal.storages.testcase_storage_implementation import \
    CaseStorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs["question_id"]
    request_data = kwargs["request_data"]
    testcase_details = request_data["testcase_details"]

    storage = CaseStorageImplementation()
    presenter = PresenterImplementation()

    interactor = CaseCreateOrUpdateInteractor(storage=storage, presenter=presenter)

    response = interactor.testcase_create_or_update(question_id=question_id, \
                                testcase_details=testcase_details)

    json_data = json.dumps(response)
    return HttpResponse(json_data, status=201)
