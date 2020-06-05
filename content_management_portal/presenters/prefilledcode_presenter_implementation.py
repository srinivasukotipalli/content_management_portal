from content_management_portal.interactors.presenters.prefilledcode_presenter_interface \
    import PresenterInterface

from content_management_portal.constants.exception_messages \
    import (
            INVALID_QUESTION_ID,
            INVALID_PREFILLED_CODE,
            INVALID_PREFILLED_CODE_FOR_QUESTION
            )

from django_swagger_utils.drf_server.exceptions import NotFound
from typing import List
from content_management_portal.interactors.storages.dtos import PrefilledCodeDto

class PresenterImplementation(PresenterInterface):

    def raise_invalid_question_exception(self):
        raise NotFound(*INVALID_QUESTION_ID)

    def raise_invalid_prefilledcode_exception(self):
        raise NotFound(*INVALID_PREFILLED_CODE)


    def raise_invalid_prefilledcode_for_question_exception(self):
        raise NotFound(*INVALID_PREFILLED_CODE_FOR_QUESTION)


    def get_response_for_list_of_prefilledcode_dtos(self, \
            list_of_prefilledcode_dtos=List[PrefilledCodeDto]):

            response_list = []
            for dto in list_of_prefilledcode_dtos:
                response_list.append(self._convert_prefilledcode_dto_to_dict(dto))

            prefiledcode_details = {
                "prefilledcode_details": response_list
            }
            return prefiledcode_details

    @staticmethod
    def _convert_prefilledcode_dto_to_dict(dto):
        prefilledcode_dict = {
                                "prefilledcode_id": dto.prefilledcode_id,
                                "code_type": dto.code_type,
                                "code": dto.code,
                                "filename": dto.filename
                            }
        return prefilledcode_dict

