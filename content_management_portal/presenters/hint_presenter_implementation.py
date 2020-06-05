from content_management_portal.interactors. \
    presenters.hint_presenter_interface import PresenterInterface
from content_management_portal.constants.exception_messages \
    import (
            INVALID_QUESTION_ID,
            INVALID_HINT_ID,
            INVALID_HINT_FOR_QUESTION
            )
from django_swagger_utils.drf_server.exceptions import NotFound
from typing import List
from content_management_portal.interactors.storages.dtos import HintDto

class PresenterImplementation(PresenterInterface):

    def raise_invalid_question_exception(self):
        raise NotFound(*INVALID_QUESTION_ID)

    def raise_invalid_hint_exception(self):
        raise NotFound(*INVALID_HINT_ID)

    def raise_invalid_hint_for_question_exception(self):
        raise NotFound(*INVALID_HINT_FOR_QUESTION)

    def get_response_for_hint(self,hint_dto: HintDto):
        hint_details_dict = {
            "hint_id": hint_dto.hint_id,
            "title": hint_dto.title,
            "content_type": hint_dto.content_type,
            "content": hint_dto.content,
            "order_id": hint_dto.order_id,
            "question_id": hint_dto.question_id
        }
        return hint_details_dict
