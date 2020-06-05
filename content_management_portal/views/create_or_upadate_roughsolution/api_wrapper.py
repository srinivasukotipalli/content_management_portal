import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal. \
    interactors.rough_solution_create_or_update_interactor \
        import RoughSolutionCreateOrUpdateInteractor

from content_management_portal.storages.roughsolution_storage_implementation import \
    RoughStorageImplementation
from content_management_portal.presenters.roughsolution_presenter_implementation \
    import PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id=kwargs['question_id']


    requested_data = kwargs['request_data']



    storage = RoughStorageImplementation()
    presenter = PresenterImplementation()

    interactor = RoughSolutionCreateOrUpdateInteractor(
                        storage=storage,presenter=presenter)

    requested_data = requested_data["roughsolution"]

    response = interactor.rough_solution_create_or_update( \
                    question_id=question_id, \
                        question_rough_solutions_list=requested_data)

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)
