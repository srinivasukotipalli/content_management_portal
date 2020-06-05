from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.presenters. \
    testcase_presenter_interface import PresenterInterface
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.exceptions import (
    InvalidQuestionId,
    InvalidTestCaseId,
    InvalidTestCaseForQuestion
    )
from typing import Optional, List, Dict
from content_management_portal.interactors.storages.dtos \
    import QuestionDto, TestCaseDto


class CaseCreateOrUpdateInteractor:

    def __init__(self, storage: StorageInterface, \
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def testcase_create_or_update(self, \
            question_id: int,testcase_details: Dict):

        try:
            self.storage.validate_question_id(question_id=question_id)
        except InvalidQuestionId:
            self.presenter.raise_invalid_question_exception()
            

        testcase_id = testcase_details.get('testcase_id')

        if testcase_id:

            try:
                self.storage.validate_testcase_id(testcase_id=testcase_id)
            except InvalidTestCaseId:
                self.presenter.raise_invalid_testcase_exception()

            try:
                self.storage.validate_question_testcase_match( \
                question_id=question_id, testcase_id=testcase_id)
            except InvalidTestCaseForQuestion:
                self.presenter.raise_invalid_testcase_for_question_exception()

            updated_testcase_dto = TestCaseDto(
                                    order_id=testcase_details["order_id"],
                                    input=testcase_details["input"],
                                    output=testcase_details["output"],
                                    is_hidden=testcase_details["is_hidden"],
                                    score=testcase_details["score"],
                                    testcase_id=testcase_details["testcase_id"],
                                    question_id=question_id
                                    )

            testcase_dto = self.storage.testcase_updation( \
                        question_id=question_id,
                        updated_testcase_dto=updated_testcase_dto,
                        )

        else:
            created_testcase_dto = TestCaseDto(
                                    testcase_id=None,
                                    order_id=testcase_details.get("order_id"),
                                    input=testcase_details["input"],
                                    output=testcase_details["output"],
                                    is_hidden=testcase_details["is_hidden"],
                                    score=testcase_details["score"],
                                    question_id=question_id
                                    )
            testcase_dto = self.storage.testcase_creation( \
                        question_id=question_id,
                        created_testcase_dto=created_testcase_dto,
                        )

        testcase_dict = self.presenter.get_response_for_testcase(
                                testcase_dto=testcase_dto
                                )
        return testcase_dict
