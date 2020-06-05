import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.testcase_deletion_interactor \
    import CaseDeletionInteractor
from content_management_portal.storages.testcase_storage_implementation \
    import CaseStorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs['question_id']
    testcase_id = kwargs['testcase_id']

    storage = CaseStorageImplementation()
    interactor = CaseDeletionInteractor(storage=storage)

    response = interactor.testcase_deletion(question_id=question_id, \
                                    testcase_id=testcase_id)

    json_data = json.dumps(response)
    return HttpResponse(json_data, status=201)
