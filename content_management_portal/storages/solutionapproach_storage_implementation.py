from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.models import SolutionApproach, Question
from content_management_portal.exceptions import (
    InvalidSolutionApproachId,
    InvalidSolutionApproachForQuestion,
    InvalidQuestionId
    )
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,SolutionApproachDto
from typing import Optional,List, Dict


class SolutionApproachStorageImplementation(StorageInterface):

    def validate_question_id(self,question_id: int):
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId

    def validate_solutionapproach_id(self,solutionapproach_id: int)->bool:
        solutionapproach = SolutionApproach.objects.filter( \
                                    id=solutionapproach_id).first()
                                    
        solutionapproach_id = solutionapproach.id
        invalid_solutionapproach_id = not solutionapproach_id
        
        if invalid_solutionapproach_id:
            raise InvalidSolutionApproachId
        else:
            return True

    def validate_question_solutionapproach_match(self, \
                        question_id: int,
                        solutionapproach_id: int
                        )->bool:

            solutionapproach_obj = SolutionApproach.objects.filter( \
                    id=solutionapproach_id, question_id=question_id).first()
                    
            invalid_solutionapproach = not solutionapproach_obj
            if invalid_solutionapproach:
                raise InvalidSolutionApproachForQuestion
            else:
                return True


    def solutionapproach_creation(self,question_id:int, \
                            created_solutionapproach_dto:SolutionApproachDto) \
                                    ->SolutionApproachDto:

        created_solutionapproach_object = \
            SolutionApproach.objects.create(
                title=created_solutionapproach_dto.title,
                description_content_type= \
                    created_solutionapproach_dto.description_content_type,
                description_content=\
                    created_solutionapproach_dto.description_content,
                complexity_analysis_content_type= \
                    created_solutionapproach_dto.complexity_analysis_content_type,
                complexity_analysis_content= \
                    created_solutionapproach_dto.complexity_analysis_content,
                question_id=question_id
                )
        solutionapproach_dto=self._convert_solutionapproach_obj_to_dto( \
                                            created_solutionapproach_object)
        return solutionapproach_dto

    def solutionapproach_updation(self,question_id: int, \
                            updated_solutionapproach_dto: SolutionApproachDto) \
                                    ->SolutionApproachDto:


        solutionapproach_obj = SolutionApproach.objects.get( \
                    id=updated_solutionapproach_dto.solutionapproach_id)

        solutionapproach_obj.title = updated_solutionapproach_dto.title
        
        solutionapproach_obj.description_content_type = \
                        updated_solutionapproach_dto.description_content_type
        solutionapproach_obj.description_content = \
                                updated_solutionapproach_dto.description_content
        solutionapproach_obj.complexity_analysis_content_type = \
                updated_solutionapproach_dto.complexity_analysis_content_type
        solutionapproach_obj.description_content = \
                updated_solutionapproach_dto.complexity_analysis_content
        solutionapproach_obj.question_id = question_id

        solutionapproach_obj.save()

        solutionapproach_dto = self._convert_solutionapproach_obj_to_dto(solutionapproach_obj)
        return solutionapproach_dto

    def solutionapproach_deletion(self,question_id:int,solutionapproach_id:int):
        SolutionApproach.objects.filter( \
            id=solutionapproach_id,question_id=question_id).delete()


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
