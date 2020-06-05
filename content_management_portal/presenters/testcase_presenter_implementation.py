from content_management_portal.interactors. \
    presenters.testcase_presenter_interface import PresenterInterface
from content_management_portal.constants.exception_messages \
    import (
            INVALID_QUESTION_ID,
            INVALID_TESTCASE_ID,
            INVALID_TESTCASE_FOR_QUESTION
            )
from django_swagger_utils.drf_server.exceptions import NotFound
from typing import List
from content_management_portal.interactors.storages.dtos import TestCaseDto

class PresenterImplementation(PresenterInterface):

    def raise_invalid_question_exception(self):
        raise NotFound(*INVALID_QUESTION_ID)
    
    def raise_invalid_testcase_exception(self):
        raise NotFound(*INVALID_TESTCASE_ID)

    def raise_invalid_testcase_for_question_exception(self):
        raise NotFound(*INVALID_TESTCASE_FOR_QUESTION)

    def get_response_for_testcase(self,testcase_dto: TestCaseDto):
        testcase_details_dict = {
            "testcase_id": testcase_dto.testcase_id,
            "order_id": testcase_dto.order_id,
            "input": testcase_dto.input,
            "output": testcase_dto.output,
            "is_hidden": testcase_dto.is_hidden,
            "score": testcase_dto.score,
            "question_id": testcase_dto.question_id
        }
        return testcase_details_dict
