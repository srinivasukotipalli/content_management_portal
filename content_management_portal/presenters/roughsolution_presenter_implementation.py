from content_management_portal.interactors.presenters.roughsolution_presenter_interface \
    import PresenterInterface

from content_management_portal.constants.exception_messages \
    import (
            INVALID_QUESTION_ID,
            INVALID_ROUGHSOLUTION_IDS,
            INVALID_ROUGH_SOLUTION_FOR_QUESTION
            )

from django_swagger_utils.drf_server.exceptions import NotFound
from typing import List
from content_management_portal.interactors.storages.dtos import RoughSolutionDto

class PresenterImplementation(PresenterInterface):

    def raise_invalid_question_exception(self):
        raise NotFound(*INVALID_QUESTION_ID)

    def raise_invalid_rough_solution_exception(self):
        raise NotFound(*INVALID_ROUGHSOLUTION_IDS)

    def raise_invalid_rough_solution_for_question_exception(self):
        raise NotFound(*INVALID_ROUGH_SOLUTION_FOR_QUESTION)
    
    def get_response_for_list_of_rough_solutions_dtos( \
            self,list_of_rough_solution_dtos: List[RoughSolutionDto]):
            response_list = []
            for dto in list_of_rough_solution_dtos:
                response_list.append(self._convert_roughsolution_dto_to_dict(dto))
            
            roughsolution_complete_details = {
                "roughsolution_complete_details": response_list
            }
            return roughsolution_complete_details

    @staticmethod
    def _convert_roughsolution_dto_to_dict(dto):
        roughsolution_dict = {  
                                "roughsolution_id": dto.roughsolution_id,
                                "code_type": dto.code_type,
                                "code": dto.code,
                                "filename": dto.filename
                            }
        return roughsolution_dict
