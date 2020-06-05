from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.presenters. \
    prefilledcode_presenter_interface import PresenterInterface
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.exceptions import (
    InvalidPrefilledCodeId,
    InvalidQuestionId,
    InvalidPrefilledCodeForQuestion,
    )
from typing import Optional, List, Dict
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,PrefilledCodeDto


class PrefilledCodeCreateOrUpdateInteractor:

    def __init__(self, storage: StorageInterface, \
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def prefilledcode_create_or_update(self, \
            question_id: int,question_prefilledcode_list:List[Dict]):

        try:
            self.storage.validate_question_id(question_id=question_id)
        except InvalidQuestionId:
            self.presenter.raise_invalid_question_exception()

        updated_prefilledcodes = []
        created_prefilledcodes = []
        list_of_prefilledcode_ids = []

        for prefilledcode in question_prefilledcode_list:
            prefilledcode_id = prefilledcode.get('prefilledcode_id')
            if prefilledcode_id:
                updated_prefilledcodes.append(prefilledcode)
                list_of_prefilledcode_ids.append(prefilledcode_id)
            else:
                created_prefilledcodes.append(prefilledcode)

        try:
            self.storage.validate_prefilledcode_ids( \
                list_of_prefilledcode_ids=list_of_prefilledcode_ids)
        except InvalidPrefilledCodeId:
            self.presenter.raise_invalid_prefilledcode_exception()

        try:
            self.storage.validate_question_prefilledcode_match( \
                        question_id=question_id, \
                        list_of_prefilledcode_ids=list_of_prefilledcode_ids)
        except InvalidPrefilledCodeForQuestion:
            self.presenter.raise_invalid_prefilledcode_for_question_exception()

        created_prefilledcode_dtos = [
                                PrefilledCodeDto(
                                    prefilledcode_id=None,
                                    code_type=prefilledcode["code_type"],
                                    code=prefilledcode["code"],
                                    filename=prefilledcode["filename"],
                                    question_id=question_id
                                    )
                                    for prefilledcode in created_prefilledcodes
                                ]

        updated_prefilledcode_dtos = [
                                PrefilledCodeDto(
                                    code_type=prefilledcode["code_type"],
                                    code=prefilledcode["code"],
                                    filename=prefilledcode["filename"],
                                    prefilledcode_id=prefilledcode["prefilledcode_id"],
                                    question_id=question_id
                                    )
                                    for prefilledcode in updated_prefilledcodes
                                ]

        list_of_prefilledcode_dtos = \
                self.storage.updation_and_creation_of_prefilledcodes( \
                        question_id=question_id,
                        updated_prefilledcode_dtos=updated_prefilledcode_dtos,
                        created_prefilledcode_dtos=created_prefilledcode_dtos
                        )

        return self.presenter.get_response_for_list_of_prefilledcode_dtos(
                    list_of_prefilledcode_dtos=list_of_prefilledcode_dtos
                    )
