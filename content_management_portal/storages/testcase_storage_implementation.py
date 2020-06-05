from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.models import Case, Question
from content_management_portal.exceptions import (
    InvalidTestCaseId,
    InvalidTestCaseForQuestion,
    InvalidQuestionId
    )
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,TestCaseDto
from typing import Optional,List, Dict


class CaseStorageImplementation(StorageInterface):

    def validate_question_id(self,question_id: int):
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId

    def validate_testcase_id(self,testcase_id: int)->bool:
        testcase = Case.objects.filter(id=testcase_id).first()
        invalid_testcase = not testcase.id
        testcase_id = testcase.id
        if invalid_testcase:
            raise InvalidTestCaseId
        else:
            return True

    def validate_question_testcase_match(self, \
                        question_id: int,
                        testcase_id: int
                        )->bool:
            testcase_obj = Case.objects.filter(id=testcase_id, \
                                            question_id=question_id).first()
            invalid_testcase = not testcase_obj
            if invalid_testcase:
                raise InvalidTestCaseForQuestion
            else:
                return True


    def testcase_creation(self,question_id:int, \
                            created_testcase_dto:TestCaseDto)->TestCaseDto:

                created_testcase_object = \
                            Case.objects.create(
                                    order_id=created_testcase_dto.order_id,
                                    input=created_testcase_dto.input,
                                    output=created_testcase_dto.output,
                                    is_hidden=created_testcase_dto.is_hidden,
                                    score=created_testcase_dto.score,
                                    question_id=question_id
                                    )

                testcase_dto = self._convert_testcase_obj_to_dto( \
                                                    created_testcase_object)
                return testcase_dto

    def testcase_updation(self,question_id:int, \
                            updated_testcase_dto:TestCaseDto)->TestCaseDto:


        testcase_obj = Case.objects.get(id=updated_testcase_dto.testcase_id)
        testcase_obj.order_id = updated_testcase_dto.order_id
        testcase_obj.input = updated_testcase_dto.input
        testcase_obj.output = updated_testcase_dto.output
        testcase_obj.is_hidden = updated_testcase_dto.is_hidden
        testcase_obj.score = updated_testcase_dto.score
        testcase_obj.question_id = question_id

        testcase_obj.save()

        testcase_dto = self._convert_testcase_obj_to_dto(testcase_obj)
        return testcase_dto

    def testcase_deletion(self,question_id:int,testcase_id:int):
        Case.objects.filter(id=testcase_id,question_id=question_id).delete()


    @staticmethod
    def _convert_testcase_obj_to_dto(obj):
        testcase_dto =TestCaseDto(
                                    order_id=obj.order_id,
                                    input=obj.input,
                                    output=obj.output,
                                    score=obj.score,
                                    is_hidden=obj.is_hidden,
                                    testcase_id=obj.id,
                                    question_id=obj.question_id
                                    )
        return testcase_dto
