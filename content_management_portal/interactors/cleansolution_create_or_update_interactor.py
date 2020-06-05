from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.presenters. \
    cleansolution_presenter_interface import PresenterInterface
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.exceptions import (
    InvalidCleanSolutionId,
    InvalidQuestionId,
    InvalidCleanSolutionForQuestion,
    )
from typing import Optional, List, Dict
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,CleanSolutionDto


class CleanSolutionCreateOrUpdateInteractor:

    def __init__(self, storage: StorageInterface, \
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def cleansolution_create_or_update(self, \
            question_id: int,question_cleansolution_list:List[Dict]):

        try:
            self.storage.validate_question_id(question_id=question_id)
        except InvalidQuestionId:
            self.presenter.raise_invalid_question_exception()

        updated_cleansolutions = []
        created_cleansolutions = []
        list_of_cleansolution_ids = []

        for cleansolution in question_cleansolution_list:
            cleansolution_id = cleansolution.get('cleansolution_id')
            if cleansolution_id:
                updated_cleansolutions.append(cleansolution)
                list_of_cleansolution_ids.append(cleansolution_id)
            else:
                created_cleansolutions.append(cleansolution)

        try:
            self.storage.validate_cleansolution_ids( \
                list_of_cleansolution_ids=list_of_cleansolution_ids)
        except InvalidCleanSolutionId:
            self.presenter.raise_invalid_prefilledcode_exception()

        try:
            self.storage.validate_question_cleansolution_match( \
                        question_id=question_id, \
                        list_of_cleansolution_ids=list_of_cleansolution_ids)
        except InvalidCleanSolutionForQuestion:
            self.presenter.raise_invalid_cleansolution_for_question_exception()

        created_cleansolution_dtos = [
                                CleanSolutionDto(
                                    cleansolution_id=None,
                                    code_type=cleansolution["code_type"],
                                    code=cleansolution["code"],
                                    filename=cleansolution["filename"],
                                    question_id=question_id
                                    )
                                    for cleansolution in created_cleansolutions
                                ]

        updated_cleansolution_dtos = [
                                CleanSolutionDto(
                                    code_type=cleansolution["code_type"],
                                    code=cleansolution["code"],
                                    filename=cleansolution["filename"],
                                    cleansolution_id=cleansolution["cleansolution_id"],
                                    question_id=question_id
                                    )
                                    for cleansolution in updated_cleansolutions
                                ]

        list_of_cleansolution_dtos = \
                self.storage.updation_and_creation_of_cleansolutions( \
                        question_id=question_id,
                        updated_cleansolution_dtos=updated_cleansolution_dtos,
                        created_cleansolution_dtos=created_cleansolution_dtos
                        )

        return self.presenter.get_response_for_list_of_cleansolution_dtos(
                    list_of_cleansolution_dtos=list_of_cleansolution_dtos
                    )
