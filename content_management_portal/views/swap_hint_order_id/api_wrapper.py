import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.swap_hint_orders_interactor \
    import SwapHintInteractor
from content_management_portal.presenters.swap_hint_presenter_implementation \
    import PresenterImplementation
from content_management_portal.storages.swap_hints_for_testcase_numbers \
    import SwapHintStorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs["question_id"]
    swap_hint_details = kwargs["request_data"]

    storage = SwapHintStorageImplementation()
    presenter = PresenterImplementation()

    interactor = SwapHintInteractor(storage=storage, presenter=presenter)

    interactor.swap_hint_numbers(question_id=question_id, \
                    swap_hint_details=swap_hint_details)
