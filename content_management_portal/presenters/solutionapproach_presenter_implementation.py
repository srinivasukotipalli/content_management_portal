from content_management_portal.interactors. \
    presenters.solutionapproach_presenter_interface import PresenterInterface
from content_management_portal.constants.exception_messages \
    import (
            INVALID_QUESTION_ID,
            INVALID_SOLUTIONAPPROACH_ID,
            INVALID_SOLUTIONAPPROACH_FOR_QUESTION
            )
from django_swagger_utils.drf_server.exceptions import NotFound
from typing import List
from content_management_portal.interactors.storages.dtos \
    import SolutionApproachDto

class PresenterImplementation(PresenterInterface):

    def raise_invalid_question_exception(self):
        raise NotFound(*INVALID_QUESTION_ID)

    def raise_invalid_solutionapproach_exception(self):
        raise NotFound(*INVALID_SOLUTIONAPPROACH_ID)

    def raise_invalid_solutionapproach_for_question_exception(self):
        raise NotFound(*INVALID_SOLUTIONAPPROACH_FOR_QUESTION)

    def get_response_for_solutionapproach(self, \
                            solutionapproach_dto: SolutionApproachDto):
        solutionapproach_details_dict = {
            "solutionapproach_id": solutionapproach_dto.solutionapproach_id,
            "title": solutionapproach_dto.title,
            "description_content_type": \
                        solutionapproach_dto.description_content_type,
            "description_content": solutionapproach_dto.description_content,
            "complexity_analysis_content_type": \
                        solutionapproach_dto.complexity_analysis_content_type,
            "complexity_analysis_content": \
                        solutionapproach_dto.complexity_analysis_content,
        }
        return solutionapproach_details_dict
