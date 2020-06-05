import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.solutionapproach_create_or_update_interactor \
    import SolutionapproachCreateOrUpdateInteractor
from content_management_portal.presenters.solutionapproach_presenter_implementation \
    import PresenterImplementation
from content_management_portal.storages.solutionapproach_storage_implementation \
    import SolutionApproachStorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs["question_id"]
    request_data = kwargs["request_data"]
    solutionapproach_details = request_data["solution_approach_details"]

    storage = SolutionApproachStorageImplementation()
    presenter = PresenterImplementation()

    interactor = SolutionapproachCreateOrUpdateInteractor( \
                                        storage=storage, presenter=presenter)

    response = interactor.solutionapproach_create_or_update( \
                            question_id=question_id, \
                                solutionapproach_details=solutionapproach_details)

    json_data = json.dumps(response)
    return HttpResponse(json_data, status=201)
