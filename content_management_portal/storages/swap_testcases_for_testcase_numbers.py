from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.models import Case, Question
from content_management_portal.exceptions import (
    InvalidTestCaseId,
    InvalidTestCaseForQuestion,
    InvalidQuestionId
    )
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,SwapTestCaseDto
from typing import Optional,List, Dict


class SwapTestCaseStorageImplementation(StorageInterface):

    def validate_question_id(self,question_id: int):
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId

    def validate_testcase_ids(
            self, first_testcase_id: int, second_testcase_id: int)->bool:

        testcase_queryset = Case.objects.filter( \
                        id__in=[first_testcase_id,second_testcase_id])

        valid_testcase_ids = len(testcase_queryset) == 2
        
        if not valid_testcase_ids:
            raise InvalidTestCaseId

    def validate_question_testcases_match(self, \
                        question_id: int,
                        first_testcase_id: int,
                        second_testcase_id: int
                        )->bool:
            testcase_queryset = Case.objects.filter( \
                                id__in=[first_testcase_id,second_testcase_id],
                                question_id=question_id
                            )
            valid_testcase_ids = len(testcase_queryset) == 2

            if not valid_testcase_ids:
                raise InvalidTestCaseForQuestion


    def swap_testcase_numbers_for_testcases(self, 
        question_id:int,swap_dto:SwapTestCaseDto)->SwapTestCaseDto:

        first_testcase_obj = Case.objects.get(id=swap_dto.first_testcase_id)
        first_testcase_obj.order_id = swap_dto.second_testcase_number
        first_testcase_obj.save()

        second_testcase_obj = Case.objects.get(id=swap_dto.second_testcase_id)
        second_testcase_obj.order_id = swap_dto.first_testcase_number
        second_testcase_obj.save()
