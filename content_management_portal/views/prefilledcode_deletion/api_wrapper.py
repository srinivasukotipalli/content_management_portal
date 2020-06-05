import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal. \
    interactors.prefilledcode_delete_interactor \
        import PrefilledCodeDeletionInteractor
from content_management_portal.storages.prefilledcode_storage_implementation import \
    PrefilledCodeStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs['question_id']
    prefilledcode_id=kwargs['prefilledcode_id']
    storage = PrefilledCodeStorageImplementation()
    interactor = PrefilledCodeDeletionInteractor(storage=storage)
    response = interactor.prefilledcode_deletion( \
                    question_id=question_id,prefilledcode_id=prefilledcode_id)

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)
