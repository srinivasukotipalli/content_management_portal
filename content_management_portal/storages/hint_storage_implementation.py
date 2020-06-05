from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.models import Hint, Question
from content_management_portal.exceptions import (
    InvalidHintId,
    InvalidHintForQuestion,
    InvalidQuestionId
    )
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,HintDto
from typing import Optional,List, Dict


class HintStorageImplementation(StorageInterface):

    def validate_question_id(self,question_id: int):
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId

    def validate_hint_id(self,hint_id: int)->bool:
        hint = Hint.objects.filter(id=hint_id).first()
        invalid_hint = not hint.id
        hint_id = hint.id
        if invalid_hint:
            raise InvalidHintId
        else:
            return True

    def validate_question_hint_match(self, \
                        question_id: int,
                        hint_id: int
                        )->bool:

            hint_obj = Hint.objects.filter(id=hint_id, \
                                            question_id=question_id).first()
            invalid_hint = not hint_obj
            if invalid_hint:
                raise InvalidHintForQuestion
            else:
                return True


    def hint_creation(self,question_id:int, \
                            created_hint_dto:HintDto)->HintDto:

                created_hint_object = \
                            Hint.objects.create(
                                    title=created_hint_dto.title,
                                    content_type=created_hint_dto.content_type,
                                    content=created_hint_dto.content,
                                    order_id=created_hint_dto.order_id,
                                    question_id=question_id
                                    )

                hint_dto = self._convert_hint_obj_to_dto( \
                                                    created_hint_object)
                return hint_dto

    def hint_updation(self,question_id: int, \
                            updated_hint_dto: HintDto)->HintDto:


        hint_obj = Hint.objects.get(id=updated_hint_dto.hint_id)

        hint_obj.title = updated_hint_dto.title
        hint_obj.content_type = updated_hint_dto.content_type
        hint_obj.content = updated_hint_dto.content
        hint_obj.order_id = updated_hint_dto.order_id
        hint_obj.question_id = question_id

        hint_obj.save()

        hint_dto = self._convert_hint_obj_to_dto(hint_obj)
        return hint_dto

    def hint_deletion(self,question_id:int,hint_id:int):
        Hint.objects.filter(id=hint_id,question_id=question_id).delete()


    @staticmethod
    def _convert_hint_obj_to_dto(obj):
        hint_dto =HintDto(
                            title=obj.title,
                            content_type=obj.content_type,
                            content=obj.content,
                            order_id=obj.order_id,
                            hint_id=obj.id,
                            question_id=obj.question_id
                        )
        return hint_dto
