import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal. \
    interactors.cleansolution_deletion_interactor \
        import CleanSolutionDeletionInteractor
from content_management_portal.storages.cleansolution_storage_implementation import \
    CleanSolutionStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs['question_id']
    cleansolution_id=kwargs['cleansolution_id']
    storage = CleanSolutionStorageImplementation()
    interactor = CleanSolutionDeletionInteractor(storage=storage)
    response = interactor.cleansolution_deletion( \
                    question_id=question_id,cleansolution_id=cleansolution_id)

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)
