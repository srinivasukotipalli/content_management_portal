from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface

class HintDeletionInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def hint_deletion(self,question_id:int, hint_id:int):
        self.storage.hint_deletion( \
                        question_id=question_id,
                        hint_id=hint_id
                        )
