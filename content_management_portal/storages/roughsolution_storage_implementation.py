from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.constants.enums import (TextType,CodeLanguage)
from content_management_portal.models import RoughSolution, Question
from content_management_portal.exceptions import (
    InvalidRoughSolutionId,
    InvalidRoughSolutionForQuestion,
    InvalidQuestionId
    )
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,RoughSolutionDto
from typing import Optional,List, Dict


class RoughStorageImplementation(StorageInterface):
    
    def validate_question_id(self,question_id: int):
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId

    def validate_rough_solution_ids(self,list_of_rough_solutions_ids: int):
        list_of_objects = RoughSolution.objects.filter(id__in=list_of_rough_solutions_ids)
        if len(list_of_objects) != len(list_of_rough_solutions_ids):
            raise InvalidRoughSolutionId

    def validate_question_roughsolutions_match(self, \
                        question_id: int,
                        list_of_rough_solutions_ids: List[int]
                        ):
            roughsolutions_list = RoughSolution.objects.values_list('id',flat=True). \
                                filter(id__in=list_of_rough_solutions_ids, \
                                        question_id=question_id
                                        )
            
            if len(roughsolutions_list) != len(list_of_rough_solutions_ids):
                raise InvalidRoughSolutionForQuestion


    def updation_and_creation_of_rough_solutions(self,question_id:int, \
                updated_rough_solutions_dtos:List[RoughSolutionDto],
                created_rough_solutions_dtos:List[RoughSolutionDto]
                )->List[RoughSolutionDto]:

                    created_rough_solutions_objs_list = [
                                RoughSolution(
                                    code_type=roughsolution.code_type,
                                    code=roughsolution.code,
                                    filename=roughsolution.filename,
                                    question_id=question_id,
                                    )
                                    for roughsolution in created_rough_solutions_dtos
                                ]
                    
                    
                    
                    updated_rough_solutions_objs_list = [
                                RoughSolution(
                                    code_type=roughsolution.code_type,
                                    code=roughsolution.code,
                                    filename=roughsolution.filename,
                                    question_id=question_id,
                                    id=roughsolution.roughsolution_id
                                    )
                                    for roughsolution in updated_rough_solutions_dtos
                                ]

                    RoughSolution.objects.bulk_create(created_rough_solutions_objs_list)
                    #print(RoughSolution.objects.all())
                    
                    RoughSolution.objects.bulk_update( \
                            updated_rough_solutions_objs_list, \
                                ['code_type','code','filename','question_id'])
                    
                    #print(RoughSolution.objects.all())
                    
                    roughsolution_objs = RoughSolution.objects.filter( \
                                                    question_id=question_id)
                    return self._convert_roughsolution_list_obj_to_dtos(roughsolution_objs)
                    
    def rough_solution_deletion(self,question_id:int,rough_solution_id:int):
        RoughSolution.objects.filter( \
                id=rough_solution_id,question_id=question_id).delete()
    

    def _convert_roughsolution_list_obj_to_dtos(self,roughsolution_objs):
        list_of_rough_solution_dtos = [RoughSolutionDto(
                                        code_type=obj.code_type,
                                        code=obj.code,
                                        filename=obj.filename,
                                        question_id=obj.question_id,
                                        roughsolution_id=obj.id
                                    )
                                    for obj in roughsolution_objs]
        return list_of_rough_solution_dtos
