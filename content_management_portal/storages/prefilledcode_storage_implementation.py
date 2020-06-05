from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.constants.enums import (TextType,CodeLanguage)
from content_management_portal.models import PrefilledCode, Question
from content_management_portal.exceptions import (
    InvalidPrefilledCodeId,
    InvalidPrefilledCodeForQuestion,
    InvalidQuestionId
    )
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,PrefilledCodeDto
from typing import Optional,List, Dict


class PrefilledCodeStorageImplementation(StorageInterface):
    
    def validate_question_id(self,question_id: int):
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId

    def validate_prefilledcode_ids(self,list_of_prefilledcode_ids: int):
        list_of_objects = PrefilledCode.objects.filter(id__in=list_of_prefilledcode_ids)
        if len(list_of_objects) != len(list_of_prefilledcode_ids):
            raise InvalidPrefilledCodeId

    def validate_question_prefilledcode_match(self, \
                        question_id: int,
                        list_of_prefilledcode_ids: List[int]
                        ):
            prefilledcode_list = PrefilledCode.objects.values_list('id',flat=True). \
                                filter(id__in=list_of_prefilledcode_ids, \
                                        question_id=question_id
                                        )
            
            if len(prefilledcode_list) != len(list_of_prefilledcode_ids):
                raise InvalidPrefilledCodeForQuestion


    def updation_and_creation_of_prefilledcodes(self,question_id:int, \
                updated_prefilledcode_dtos:List[PrefilledCodeDto],
                created_prefilledcode_dtos:List[PrefilledCodeDto]
                )->List[PrefilledCodeDto]:
                    print(created_prefilledcode_dtos)
                    created_prefilledcode_objs_list = [
                                PrefilledCode(
                                    code_type=prefilledcode.code_type,
                                    code=prefilledcode.code,
                                    filename=prefilledcode.filename,
                                    question_id=question_id,
                                    )
                                    for prefilledcode in created_prefilledcode_dtos
                                ]
                    
                    print(updated_prefilledcode_dtos,"A"*50,)
                    updated_prefilledcode_objs_list = [
                                PrefilledCode(
                                    code_type=prefilledcode.code_type,
                                    code=prefilledcode.code,
                                    filename=prefilledcode.filename,
                                    question_id=question_id,
                                    id=prefilledcode.prefilledcode_id
                                    )
                                    for prefilledcode in updated_prefilledcode_dtos
                                ]

                    PrefilledCode.objects.bulk_create(created_prefilledcode_objs_list)
                    #print(RoughSolution.objects.all())
                    
                    PrefilledCode.objects.bulk_update( \
                            updated_prefilledcode_objs_list, \
                                ['code_type','code','filename','question_id'])
                    
                    #print(RoughSolution.objects.all())
                    
                    prefilledcode_objs = PrefilledCode.objects.filter( \
                                                    question_id=question_id)
                    return self._convert_prefilledcode_list_obj_to_dtos(prefilledcode_objs)
                    
    def prefilledcode_deletion(self,question_id:int,prefilledcode_id:int):
        PrefilledCode.objects.filter( \
                id=prefilledcode_id,question_id=question_id).delete()
    

    @staticmethod
    def _convert_prefilledcode_list_obj_to_dtos(prefilledcode_objs):
        list_of_prefilledcode_dtos = [PrefilledCodeDto(
                                        code_type=obj.code_type,
                                        code=obj.code,
                                        filename=obj.filename,
                                        question_id=obj.question_id,
                                        prefilledcode_id=obj.id
                                    )
                                    for obj in prefilledcode_objs]
        return list_of_prefilledcode_dtos
