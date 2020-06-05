from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.constants.enums import TextType,CodeLanguage
from content_management_portal.models import CleanSolution, Question
from content_management_portal.exceptions import (
    InvalidCleanSolutionId,
    InvalidCleanSolutionForQuestion,
    InvalidQuestionId
    )
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,CleanSolutionDto
from typing import Optional,List, Dict


class CleanSolutionStorageImplementation(StorageInterface):

    def validate_question_id(self,question_id: int):
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId

    def validate_cleansolution_ids(self,list_of_cleansolution_ids: int):
        list_of_objects = CleanSolution.objects.filter(id__in=list_of_cleansolution_ids)
        if len(list_of_objects) != len(list_of_cleansolution_ids):
            raise InvalidCleanSolutionId


    def validate_question_cleansolution_match(self, \
                        question_id: int,
                        list_of_cleansolution_ids: List[int]
                        ):
            cleansolution_list = CleanSolution.objects.values_list('id',flat=True). \
                                filter(id__in=list_of_cleansolution_ids, \
                                        question_id=question_id
                                        )

            if len(cleansolution_list) != len(list_of_cleansolution_ids):
                raise InvalidCleanSolutionForQuestion


    def updation_and_creation_of_cleansolutions(self,question_id:int, \
                updated_cleansolution_dtos:List[CleanSolutionDto],
                created_cleansolution_dtos:List[CleanSolutionDto]
                )->List[CleanSolutionDto]:

                    created_cleansolution_objs_list = [
                                CleanSolution(
                                    code_type=cleansolution.code_type,
                                    code=cleansolution.code,
                                    filename=cleansolution.filename,
                                    question_id=question_id,
                                    )
                                    for cleansolution in created_cleansolution_dtos
                                ]

                    updated_cleansolution_objs_list = [
                                CleanSolution(
                                    code_type=cleansolution.code_type,
                                    code=cleansolution.code,
                                    filename=cleansolution.filename,
                                    question_id=question_id,
                                    id=cleansolution.cleansolution_id
                                    )
                                    for cleansolution in updated_cleansolution_dtos
                                ]

                    CleanSolution.objects.bulk_create(created_cleansolution_objs_list)
                    CleanSolution.objects.bulk_update( \
                            updated_cleansolution_objs_list, \
                                ['code_type','code','filename','question_id'])

                    cleansolution_objs = CleanSolution.objects.filter( \
                                                    question_id=question_id)
                    return self._convert_cleansolution_list_obj_to_dtos(cleansolution_objs)


    def cleansolution_deletion(self,question_id:int,cleansolution_id:int):
        CleanSolution.objects.filter( \
                id=cleansolution_id,question_id=question_id).delete()


    @staticmethod
    def _convert_cleansolution_list_obj_to_dtos(cleansolution_objs):
        list_of_cleansolution_dtos = [CleanSolutionDto(
                                        code_type=obj.code_type,
                                        code=obj.code,
                                        filename=obj.filename,
                                        question_id=obj.question_id,
                                        cleansolution_id=obj.id
                                    )
                                    for obj in cleansolution_objs]
        return list_of_cleansolution_dtos
