from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.models import Hint, Question
from content_management_portal.exceptions import (
    InvalidHintId,
    InvalidHintForQuestion,
    InvalidQuestionId
    )
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,SwapHintDto
from typing import Optional,List, Dict


class SwapHintStorageImplementation(StorageInterface):

    def validate_question_id(self,question_id: int):
        try:
            Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            raise InvalidQuestionId

    def validate_hint_ids(
            self, first_hint_id: int, second_hint_id: int)->bool:

        hint_queryset = Hint.objects.filter( \
                        id__in=[first_hint_id,second_hint_id])

        valid_hint_ids = len(hint_queryset) == 2

        if not valid_hint_ids:
            raise InvalidHintId

    def validate_question_hints_match(self, \
                        question_id: int,
                        first_hint_id: int,
                        second_hint_id: int
                        )->bool:
            hint_queryset = Hint.objects.filter( \
                                id__in=[first_hint_id,second_hint_id],
                                question_id=question_id
                            )
            valid_hint_ids = len(hint_queryset) == 2

            if not valid_hint_ids:
                raise InvalidHintForQuestion


    def swap_hint_numbers_for_hints(self, 
        question_id:int,swap_dto:SwapHintDto)->SwapHintDto:

        first_hint_obj = Hint.objects.get(id=swap_dto.first_hint_id)
        first_hint_obj.order_id = swap_dto.second_hint_number
        first_hint_obj.save()

        second_hint_obj = Hint.objects.get(id=swap_dto.second_hint_id)
        second_hint_obj.order_id = swap_dto.first_hint_number
        second_hint_obj.save()
