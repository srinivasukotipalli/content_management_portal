from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.models import \
    (
        RoughSolution,
        Question,
        Case,
        SolutionApproach,
        CleanSolution,
        Hint,
        PrefilledCode
    )
from content_management_portal.exceptions.exceptions import InvalidQuestionId
from typing import Optional,List, Dict
from content_management_portal.interactors.storages.dtos \
    import (
                QuestionDto,
                RoughSolutionDto,
                TestCaseDto,
                CleanSolutionDto,
                SolutionApproachDto,
                PrefilledCodeDto,
                HintDto
            )


class GetQuestionStorageImplementation(StorageInterface):

    def validate_question_id(self,question_id: int):
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId

    def get_question(self, question_id: int):
        question = Question.objects.filter(id=question_id) \
                           .select_related('solution_approach') \
                           .prefetch_related(
                               'rough_solutions',
                               'test_cases',
                               'prefilled_codes',
                               'clean_solutions',
                               'hints'
                               ).first()


        question_dto = self._convert_question_obj_to_question_dto(question)

        roughsolution_queryset = question.rough_solutions.all()
        list_of_roughsolution_dtos = \
                    self._convert_roughsolution_queryset_to_dtos_list(
                                                    roughsolution_queryset)

        testcase_queryset = question.test_cases.all()
        list_of_testcase_dtos = \
                    self._convert_testcase_queryset_to_dtos_list(
                                                    testcase_queryset)

        prefilledcode_queryset = question.prefilled_codes.all()
        list_of_prefilledcode_dtos = \
                    self._convert_prefilledcode_queryset_to_dtos_list(
                                                    prefilledcode_queryset)


        try:
            solutionapproach_obj = question.solution_approach
            solutionapproach_dto = \
                    self._convert_solutionapproach_obj_to_dto(solutionapproach_obj)
        except:
            solutionapproach_dto = None

        cleansolution_queryset = question.clean_solutions.all()
        list_of_cleansolution_dtos = \
                    self._convert_cleansolution_queryset_to_dtos_list(
                                                    cleansolution_queryset)


        hint_queryset = question.hints.all()
        list_of_hint_dtos = self._convert_hint_queryset_to_dtos_list( \
                                                                hint_queryset)

        return question_dto, list_of_roughsolution_dtos, list_of_testcase_dtos, \
                list_of_prefilledcode_dtos, solutionapproach_dto, \
                list_of_cleansolution_dtos, list_of_hint_dtos

    @staticmethod
    def _convert_question_obj_to_question_dto(question_obj):

        questiondto = QuestionDto(
            user_id=question_obj.user_id,
            short_title=question_obj.short_title,
            content_type=question_obj.content_type,
            content=question_obj.content,
            question_id=question_obj.id
            )
        return questiondto

    @staticmethod
    def _convert_roughsolution_queryset_to_dtos_list(roughsolution_queryset):

        list_of_rough_solution_dtos =  [
                                            RoughSolutionDto(
                                                code_type=obj.code_type,
                                                code=obj.code,
                                                filename=obj.filename,
                                                question_id=obj.question_id,
                                                roughsolution_id=obj.id
                                            )
                                            for obj in roughsolution_queryset
                                        ]
        return list_of_rough_solution_dtos

    @staticmethod
    def _convert_testcase_queryset_to_dtos_list(testcase_queryset):

        list_of_testcase_dtos =  [
                            TestCaseDto(
                                order_id=obj.order_id,
                                input=obj.input,
                                output=obj.output,
                                score=obj.score,
                                is_hidden=obj.is_hidden,
                                testcase_id=obj.id,
                                question_id=obj.question_id
                            )
                            for obj in testcase_queryset
                        ]
        return list_of_testcase_dtos

    @staticmethod
    def _convert_prefilledcode_queryset_to_dtos_list(prefilledcode_queryset):

        list_of_prefilledcode_dtos = [PrefilledCodeDto(
                                        code_type=obj.code_type,
                                        code=obj.code,
                                        filename=obj.filename,
                                        question_id=obj.question_id,
                                        prefilledcode_id=obj.id
                                    )
                                    for obj in prefilledcode_queryset]
        return list_of_prefilledcode_dtos

    @staticmethod
    def _convert_solutionapproach_obj_to_dto(obj):

        solutionapproach_dto = \
                    SolutionApproachDto(
                                        title=obj.title,
                                        description_content_type= \
                                               obj.description_content_type,
                                        description_content= \
                                                    obj.description_content,
                                        complexity_analysis_content_type= \
                                            obj.complexity_analysis_content_type,
                                        complexity_analysis_content= \
                                                obj.complexity_analysis_content,
                                        solutionapproach_id=obj.id,
                                        question_id=obj.question_id
                                        )
        return solutionapproach_dto

    @staticmethod
    def _convert_cleansolution_queryset_to_dtos_list(cleansolution_queryset):

        list_of_cleansolution_dtos = [CleanSolutionDto(
                                        code_type=obj.code_type,
                                        code=obj.code,
                                        filename=obj.filename,
                                        question_id=obj.question_id,
                                        cleansolution_id=obj.id
                                    )
                                    for obj in cleansolution_queryset]
        return list_of_cleansolution_dtos

    @staticmethod
    def _convert_hint_queryset_to_dtos_list(hint_queryset):

        hint_dto =  [HintDto(
                        title=obj.title,
                        content_type=obj.content_type,
                        content=obj.content,
                        order_id=obj.order_id,
                        hint_id=obj.id,
                        question_id=obj.question_id
                    )
                    for obj in hint_queryset]
        return hint_dto
