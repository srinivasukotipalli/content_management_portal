from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors. \
    presenters.question_presenter_interface import PresenterInterface
from content_management_portal.exceptions.exceptions import InvalidQuestionId


class QuestionUpdateInteractor:

    def __init__(self, storage: StorageInterface,
                    presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def question_updation(self,user_id: int, short_title: str, \
                content_type:TextType, content:str, question_id:int):
        
        try:
            self.storage.validate_question_id(question_id=question_id)
        except InvalidQuestionId:
            self.presenter.raise_invalid_question_exception()

        questiondto = self.storage.question_updation(
                                                        user_id=user_id,
                                                        short_title=short_title,
                                                        content_type=content_type,
                                                        content=content,
                                                        question_id=question_id
                                                    )
        return self.presenter.get_question_dto_response(
                questiondto=questiondto)
