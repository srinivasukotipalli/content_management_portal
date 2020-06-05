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


class GetQuestionImplementation(StorageInterface):

    def validate_question_id(self,question_id: int):
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId

    def get_question(self, question_id: int):
        question = Question.objects.filter(id=1) \
                           .select_related('solution_approach') \
                           .prefetch_related(
                               'rough_solutions',
                               'test_cases',
                               'prefilled_codes',
                               'clean_solutions',
                               'hints'
                               ).first()

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
        
        solutionapproach_obj = question.solution_approach
        solutionapproach_dto = \
                self._convert_solutionapproach_obj_to_dto(solutionapproach_obj)
                
        cleansolution_queryset = question.clean_solutions.all()
        list_of_cleansolution_dtos = \
                    self._convert_cleansolution_queryset_to_dtos_list(
                                                    cleansolution_queryset)

        
        hint_queryset = question.hints.all()
        list_of_hint_dtos = self._convert_hint_queryset_to_dtos_list( \
                                                                hint_queryset)

    def _convert_roughsolution_queryset_to_dtos_list(roughsolution_queryset):
        
        list_of_roughsolution_dtos =
            
            ]