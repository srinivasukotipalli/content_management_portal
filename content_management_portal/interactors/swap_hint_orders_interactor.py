from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.presenters. \
    swap_hints_presenter_interface import PresenterInterface
from content_management_portal.exceptions import (
    InvalidQuestionId,
    InvalidHintId,
    InvalidHintForQuestion
    )
from typing import Optional, List, Dict
from content_management_portal.interactors.storages.dtos \
     import SwapHintDto


class SwapHintInteractor:

    def __init__(self, storage: StorageInterface, \
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def swap_hint_numbers(self, \
            question_id: int,swap_hint_details: Dict):

        try:
            self.storage.validate_question_id(question_id=question_id)
        except InvalidQuestionId:
            self.presenter.raise_invalid_question_exception()


        first_hint_dict = swap_hint_details["first_hint"]
        second_hint_dict = swap_hint_details["second_hint"]

        first_hint_id = first_hint_dict["hint_id"]
        second_hint_id = second_hint_dict["hint_id"]
        first_hint_number = first_hint_dict["hint_number"]
        second_hint_number = second_hint_dict["hint_number"]


        try:
            self.storage.validate_hint_ids(
                first_hint_id=first_hint_id,
                second_hint_id=second_hint_id
                )
        except InvalidHintId:
            self.presenter.raise_invalid_hint_exception()

        try:
            self.storage.validate_question_hints_match( \
                question_id=question_id,
                first_hint_id=first_hint_id,
                second_hint_id=second_hint_id
                )
        except InvalidHintForQuestion:
            self.presenter.raise_invalid_hint_for_question_exception()


        swap_dto =  SwapHintDto(
                            first_hint_id=first_hint_id,
                            second_hint_id=second_hint_id,
                            first_hint_number=first_hint_number,
                            second_hint_number=second_hint_number
                            )

        self.storage.swap_hint_numbers_for_hints( \
                                            self, swap_dto=swap_dto)
