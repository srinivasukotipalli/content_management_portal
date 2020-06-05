import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.question_updation_interactor import \
    QuestionUpdateInteractor
from content_management_portal.storages.question_storage_implementation import \
    QuestionStorageImplementation
from content_management_portal.presenters.question_presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    
    
    request_data = kwargs['request_data']
    
    question_id = kwargs['question_id']
    
    #print(kwargs)
    user = kwargs['user']
    
    user_id = user.id
    
    short_title = request_data['short_title']

    content_type = request_data['problem_description']['content_type']
    
    content = request_data['problem_description']['content']

    
    storage = QuestionStorageImplementation()
    
    presenter = PresenterImplementation()
    
    interactor = QuestionUpdateInteractor(storage=storage, presenter=presenter)
    
    #print(question_id,short_title,content_type,content)
    
    response = interactor.question_updation(
                                user_id=user_id,
                                question_id=question_id,
                                short_title=short_title, 
                                content_type = content_type, 
                                content=content)
    json_data = json.dumps(response)
    
    print(json_data)
    
    return HttpResponse(json_data, status=201)

    