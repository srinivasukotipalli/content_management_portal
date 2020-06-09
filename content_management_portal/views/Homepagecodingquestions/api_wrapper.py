import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.coding_questions_interactor \
	import CodingQuestionsInteractor
from content_management_portal.storages.home_page_coding_questions_implementation \
	import HomeStorageImplementation
from content_management_portal.presenters.coding_questions_presenter_implementation \
			import PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

	requested_data = kwargs['request_query_params']

	offset = requested_data['offset']
	limit = requested_data['limit']

	storage = HomeStorageImplementation()
	presenter = PresenterImplementation()

	interactor = CodingQuestionsInteractor(storage=storage,presenter=presenter)

	response = interactor.homepage_coding_questions(offset=offset, limit=limit)

	json_data = json.dumps(response)
	return HttpResponse(json_data, status=201)
