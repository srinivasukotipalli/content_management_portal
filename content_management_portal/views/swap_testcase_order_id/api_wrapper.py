import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from content_management_portal.interactors.swap_testcase_orders_interactor \
    import SwapCasesInteractor
from content_management_portal.presenters.swap_testcase_presenter_implementation \
    import PresenterImplementation
from content_management_portal.storages.swap_testcases_for_testcase_numbers \
    import SwapTestCaseStorageImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    question_id = kwargs["question_id"]
    swap_testcase_details = kwargs["request_data"]

    storage = SwapTestCaseStorageImplementation()
    presenter = PresenterImplementation()

    interactor = SwapCasesInteractor(storage=storage, presenter=presenter)

    interactor.swap_testcase_numbers(question_id=question_id, \
                    swap_testcase_details=swap_testcase_details)
