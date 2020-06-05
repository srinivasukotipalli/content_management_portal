import json
from django.http import HttpResponse


from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


from content_management_portal.interactors.question_deletion_interactor import \
    QuestionDeletionInteractor
from content_management_portal.storages.question_storage_implementation import \
    QuestionStorageImplementation
from content_management_portal.presenters.question_presenter_implementation import \
    PresenterImplementation
    
    
@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    
    storage = QuestionStorageImplementation()
    
    question_id = kwargs['question_id']
    
    interactor = QuestionDeletionInteractor(storage=storage)
    
    response = interactor.question_deletion(question_id=question_id)
    json_data = json.dumps(response)
    
    return HttpResponse(json_data, status=201)
