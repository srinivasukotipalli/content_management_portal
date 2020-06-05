from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.presenters. \
    hint_presenter_interface import PresenterInterface
from content_management_portal.constants.enums import TextType
from content_management_portal.exceptions import (
    InvalidQuestionId,
    InvalidHintId,
    InvalidHintForQuestion
    )
from typing import Optional, List, Dict
from content_management_portal.interactors.storages.dtos \
    import QuestionDto, HintDto


class HintCreateOrUpdateInteractor:

    def __init__(self, storage: StorageInterface, \
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def hint_create_or_update(self, \
            question_id: int,hint_details: Dict):

        try:
            self.storage.validate_question_id(question_id=question_id)
        except InvalidQuestionId:
            self.presenter.raise_invalid_question_exception()

        hint_id = hint_details.get('hint_id')

        if hint_id:

            try:
                self.storage.validate_hint_id(hint_id=hint_id)
            except InvalidHintId:
                self.presenter.raise_invalid_hint_exception()

            try:
                self.storage.validate_question_hint_match( \
                question_id=question_id, hint_id=hint_id)
            except InvalidHintForQuestion:
                self.presenter.raise_invalid_hint_for_question_exception()

            updated_hint_dto = HintDto(
                                    title=hint_details["title"],
                                    content_type=hint_details["content_type"],
                                    content=hint_details["content"],
                                    order_id=hint_details.get("order_id"),
                                    hint_id=hint_details["hint_id"],
                                    question_id=question_id
                                    )

            hint_dto = self.storage.hint_updation( \
                        question_id=question_id,
                        updated_hint_dto=updated_hint_dto,
                        )

        else:
            created_hint_dto = HintDto(
                                    title=hint_details["title"],
                                    content_type=hint_details["content_type"],
                                    content=hint_details["content"],
                                    order_id=hint_details["order_id"],
                                    hint_id=None,
                                    question_id=question_id
                                    )
            hint_dto = self.storage.hint_creation( \
                        question_id=question_id,
                        created_hint_dto=created_hint_dto,
                        )

        hint_dict = self.presenter.get_response_for_hint(
                                hint_dto=hint_dto
                                )
        return hint_dict