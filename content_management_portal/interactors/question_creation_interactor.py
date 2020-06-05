from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters.question_presenter_interface \
    import PresenterInterface

class QuestionCreateInteractor:

    def __init__(self, storage: StorageInterface,
                    presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def question_creation(self, user_id: int,short_title: str, \
                content_type:TextType, content:str):
        questiondto = self.storage.question_creation(
            user_id=user_id,
            short_title=short_title,
            content_type=content_type,
            content=content
        )
        
        return self.presenter.get_question_dto_response(
                questiondto=questiondto)
