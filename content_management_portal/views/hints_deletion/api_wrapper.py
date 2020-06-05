import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.hint_deletion_interactor \
    import HintDeletionInteractor
from content_management_portal.storages.hint_storage_implementation \
    import HintStorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs['question_id']
    hint_id = kwargs['hint_id']

    storage = HintStorageImplementation()
    interactor = HintDeletionInteractor(storage=storage)

    response = interactor.hint_deletion(question_id=question_id, \
                                    hint_id=hint_id)

    json_data = json.dumps(response)
    return HttpResponse(json_data, status=201)
