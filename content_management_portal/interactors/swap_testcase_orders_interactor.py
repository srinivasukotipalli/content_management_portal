from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.presenters. \
    swap_testcases_presenter_interface import PresenterInterface
from content_management_portal.exceptions import (
    InvalidQuestionId,
    InvalidTestCaseId,
    InvalidTestCaseForQuestion
    )
from typing import Optional, List, Dict
from content_management_portal.interactors.storages.dtos \
     import SwapTestCaseDto


class SwapCasesInteractor:

    def __init__(self, storage: StorageInterface, \
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def swap_testcase_numbers(self, \
            question_id: int,swap_testcase_details: Dict):

        try:
            self.storage.validate_question_id(question_id=question_id)
        except InvalidQuestionId:
            self.presenter.raise_invalid_question_exception()


        first_testcase_dict = swap_testcase_details["first_testcase"]
        second_testcase_dict = swap_testcase_details["second_testcase"]

        first_testcase_id = first_testcase_dict["testcase_id"]
        second_testcase_id = second_testcase_dict["testcase_id"]
        first_testcase_number = first_testcase_dict["testcase_number"]
        second_testcase_number = second_testcase_dict["testcase_number"]


        try:
            self.storage.validate_testcase_ids(
                first_testcase_id=first_testcase_id,
                second_testcase_id=second_testcase_id
                )
        except InvalidTestCaseId:
            self.presenter.raise_invalid_testcase_exception()

        try:
            self.storage.validate_question_testcases_match( \
                question_id=question_id,
                first_testcase_id=first_testcase_id,
                second_testcase_id=second_testcase_id
                )
        except InvalidTestCaseForQuestion:
            self.presenter.raise_invalid_testcase_for_question_exception()


        swap_dto =  SwapTestCaseDto(
                            first_testcase_id=first_testcase_id,
                            second_testcase_id=second_testcase_id,
                            first_testcase_number=first_testcase_number,
                            second_testcase_number=second_testcase_number
                            )

        self.storage.swap_testcase_numbers_for_testcases( \
                                            self, swap_dto=swap_dto)
