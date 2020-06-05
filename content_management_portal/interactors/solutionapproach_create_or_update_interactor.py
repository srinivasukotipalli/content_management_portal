from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.presenters. \
    solutionapproach_presenter_interface import PresenterInterface
from content_management_portal.constants.enums import TextType
from content_management_portal.exceptions import (
    InvalidQuestionId,
    InvalidSolutionApproachId,
    InvalidSolutionApproachForQuestion
    )
from typing import Optional, List, Dict
from content_management_portal.interactors.storages.dtos \
    import QuestionDto, SolutionApproachDto


class SolutionapproachCreateOrUpdateInteractor:

    def __init__(self, storage: StorageInterface, \
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def solutionapproach_create_or_update(self, \
            question_id: int,solutionapproach_details: Dict):

        try:
            self.storage.validate_question_id(question_id=question_id)
        except InvalidQuestionId:
            self.presenter.raise_invalid_question_exception()

        solutionapproach_id = solutionapproach_details.get('solutionapproach_id')

        if solutionapproach_id:

            try:
                self.storage.validate_solutionapproach_id( \
                        solutionapproach_id=solutionapproach_id)
            except InvalidSolutionApproachId:
                self.presenter.raise_invalid_solutionapproach_exception()

            try:
                self.storage.validate_question_solutionapproach_match( \
                                    question_id=question_id,
                                    solutionapproach_id=solutionapproach_id)
            except InvalidSolutionApproachForQuestion:
                self.presenter.raise_invalid_solutionapproach_for_question_exception()

            updated_solutionapproach_dto = \
                    SolutionApproachDto(
                        title=solutionapproach_details["title"],
                        description_content_type= \
                            solutionapproach_details["description_content_type"],
                        description_content= \
                            solutionapproach_details["description_content"],
                        complexity_analysis_content_type= \
                            solutionapproach_details["complexity_analysis_content_type"],
                        complexity_analysis_content= \
                            solutionapproach_details["complexity_analysis_content"],
                        question_id=question_id,
                        solutionapproach_id=solutionapproach_id
                        )

            solutionapproach_dto = self.storage.solutionapproach_updation( \
                        question_id=question_id,
                        updated_solutionapproach_dto=updated_solutionapproach_dto,
                        )

        else:
            created_solutionapproach_dto = \
                    SolutionApproachDto(
                        title=solutionapproach_details["title"],
                        description_content_type= \
                            solutionapproach_details["description_content_type"],
                        description_content= \
                            solutionapproach_details["description_content"],
                        complexity_analysis_content_type= \
                            solutionapproach_details["complexity_analysis_content_type"],
                        complexity_analysis_content= \
                            solutionapproach_details["complexity_analysis_content"],
                        question_id=question_id,
                        solutionapproach_id=None
                        )            
            solutionapproach_dto = self.storage.solutionapproach_creation( \
                        question_id=question_id,
                        created_solutionapproach_dto=created_solutionapproach_dto,
                        )

        solutionapproach_dict = self.presenter.get_response_for_solutionapproach(
                                solutionapproach_dto=solutionapproach_dto
                                )
        return solutionapproach_dict