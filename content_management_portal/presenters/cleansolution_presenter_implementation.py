from content_management_portal.interactors.presenters. \
    cleansolution_presenter_interface import PresenterInterface
from content_management_portal.constants.exception_messages \
    import (
            INVALID_QUESTION_ID,
            INVALID_CLEANSOLUTION,
            INVALID_CLEAN_SOLUTION_FOR_QUESTION
            )

from django_swagger_utils.drf_server.exceptions import NotFound
from typing import List
from content_management_portal.interactors.storages.dtos import CleanSolutionDto

class PresenterImplementation(PresenterInterface):

    def raise_invalid_question_exception(self):
        raise NotFound(*INVALID_QUESTION_ID)

    def raise_invalid_cleansolution_exception(self):
        raise NotFound(*INVALID_CLEANSOLUTION)


    def raise_invalid_cleansolution_for_question_exception(self):
        raise NotFound(*INVALID_CLEAN_SOLUTION_FOR_QUESTION)


    def get_response_for_list_of_cleansolution_dtos(self, \
            list_of_cleansolution_dtos=List[CleanSolutionDto]):

            response_list = []
            for dto in list_of_cleansolution_dtos:
                response_list.append(self._convert_cleansolution_dto_to_dict(dto))

            cleansolution_details = {
                "cleansolution_details": response_list
            }
            return cleansolution_details

    @staticmethod
    def _convert_cleansolution_dto_to_dict(dto):
        cleansolution_dict = {
                                "cleansolution_id": dto.cleansolution_id,
                                "code_type": dto.code_type,
                                "code": dto.code,
                                "filename": dto.filename
                            }
        return cleansolution_dict

