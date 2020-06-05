import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.question_creation_interactor import \
    QuestionCreateInteractor
from content_management_portal.storages.question_storage_implementation import \
    QuestionStorageImplementation
from content_management_portal.presenters.question_presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    
    user = kwargs['user']
    user_id = user.id
    
    request_data = kwargs['request_data']
    
    
    short_title = request_data['short_title']

    content_type = request_data['problem_description']['content_type']
    
    content = request_data['problem_description']['content']
    
    storage = QuestionStorageImplementation()
    
    presenter = PresenterImplementation()
    
    interactor = QuestionCreateInteractor(storage=storage, presenter=presenter)
    
    response = interactor.question_creation(user_id=user_id, \
                                short_title=short_title, 
                                content_type = content_type, 
                                content=content)
    json_data = json.dumps(response)
    
    return HttpResponse(json_data, status=201)
