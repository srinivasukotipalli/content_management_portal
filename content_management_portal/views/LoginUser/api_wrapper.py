import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from content_management_portal.interactors.user_login_interactor import \
    UserLoginInteractor
from content_management_portal.storages.login_user_storage_implementation import \
    UserStorageImplementation
from content_management_portal.presenters.login_user_presenter_implementation \
    import PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']

    storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()

    interactor = UserLoginInteractor(storage=storage, \
                    presenter=presenter,oauth_storage=oauth_storage)

    response = interactor.login_user(username=username,password=password)

    json_data = json.dumps(response)

    # print(json_data)

    return HttpResponse(json_data)

