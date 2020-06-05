from content_management_portal.interactors. \
    presenters.swap_hints_presenter_interface import PresenterInterface
from content_management_portal.constants.exception_messages \
    import (
            INVALID_QUESTION_ID,
            INVALID_HINT_ID,
            INVALID_HINT_FOR_QUESTION
            )
from django_swagger_utils.drf_server.exceptions import NotFound
from typing import List
from content_management_portal.interactors.storages.dtos import SwapTestCaseDto

class PresenterImplementation(PresenterInterface):

    def raise_invalid_question_exception(self):
        raise NotFound(*INVALID_QUESTION_ID)
    
    def raise_invalid_hint_exception(self):
        raise NotFound(*INVALID_HINT_ID)

    def raise_invalid_hint_for_question_exception(self):
        raise NotFound(*INVALID_HINT_FOR_QUESTION)
