from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface

class QuestionDeletionInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def question_deletion(self,question_id:int):
        self.storage.question_deletion(
            question_id=question_id
        )
