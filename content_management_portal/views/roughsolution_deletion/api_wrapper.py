import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal. \
    interactors.rough_solution_deletion_interactor \
        import RoughSolutionDeletionInteractor
from content_management_portal.storages.roughsolution_storage_implementation import \
    RoughStorageImplementation
from content_management_portal.presenters.roughsolution_presenter_implementation \
    import PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    question_id = kwargs['question_id']
    rough_solution_id=kwargs['roughsolution_id']
    storage = RoughStorageImplementation()
    interactor = RoughSolutionDeletionInteractor(storage=storage)
    response = interactor.rough_solution_deletion( \
                    question_id=question_id,rough_solution_id=rough_solution_id)
    
    json_data = json.dumps(response)
    
    return HttpResponse(json_data, status=201)

    
    
    
    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from content_management_portal.views.roughsolution_deletion.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from content_management_portal.views.roughsolution_deletion.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from content_management_portal.views.roughsolution_deletion.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="content_management_portal", test_case=test_case,
    #     operation_name="roughsolution_deletion",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]