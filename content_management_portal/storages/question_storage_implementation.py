from content_management_portal.interactors.storages.dtos \
    import QuestionDto
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )
from content_management_portal.models import Question
from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface


class QuestionStorageImplementation(StorageInterface):

    def question_creation(self, \
                    user_id: int,
                    short_title: str,
                    content_type:TextType,
                    content:str) -> QuestionDto:

                    question_obj = Question.objects.create(
                            short_title=short_title,
                            content_type=content_type,
                            content=content,
                            user_id=user_id
                            )

                    questiondto = self._convert_question_obj_to_question_dto(question_obj)
                    return questiondto

    def question_updation(self, \
                    user_id: int,
                    short_title: str,
                    content_type:TextType,
                    content:str,
                    question_id:int) -> QuestionDto:

                    question_obj = Question.objects.get(id=question_id)
                    question_obj.short_title=short_title
                    question_obj.content_type=content_type
                    question_obj.content=content
                    question_obj.save()

                    questiondto = self._convert_question_obj_to_question_dto(question_obj)
                    return questiondto

    def question_deletion(self,question_id:int):
            Question.objects.filter(id=question_id).delete()

    @staticmethod
    def _convert_question_obj_to_question_dto(question_obj):
        #print(question_obj.id)
        questiondto = QuestionDto(
            user_id=question_obj.user_id,
            short_title=question_obj.short_title,
            content_type=question_obj.content_type,
            content=question_obj.content,
            question_id=question_obj.id
            )
        return questiondto