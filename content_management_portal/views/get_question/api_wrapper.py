import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.get_question_interactor \
    import GetQuestionInteractor
from content_management_portal.storages.get_question_storage_implementation \
    import GetQuestionStorageImplementation
from content_management_portal.presenters.getquestion_presenter_implementation \
    import PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id=kwargs['question_id']

    storage = GetQuestionStorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetQuestionInteractor(storage=storage,presenter=presenter)

    response = interactor.get_question(question_id=question_id)

    json_data = json.dumps(response)

    return HttpResponse(json_data, status=201)
