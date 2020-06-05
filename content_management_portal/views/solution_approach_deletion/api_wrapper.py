import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.solutionapproach_deletion_interactor \
    import SolutionapproachDeletionInteractor
from content_management_portal.storages.solutionapproach_storage_implementation \
    import SolutionApproachStorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs['question_id']
    solutionapproach_id = kwargs['solution_approach_id']

    storage = SolutionApproachStorageImplementation()
    interactor = SolutionapproachDeletionInteractor(storage=storage)

    response = interactor.solutionapproach_deletion(question_id=question_id, \
                                    solutionapproach_id=solutionapproach_id)

    json_data = json.dumps(response)
    return HttpResponse(json_data, status=201)
