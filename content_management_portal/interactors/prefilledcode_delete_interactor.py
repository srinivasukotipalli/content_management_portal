from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface

class PrefilledCodeDeletionInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def prefilledcode_deletion(self,question_id:int,prefilledcode_id:int):
        self.storage.prefilledcode_deletion(
            question_id=question_id,
            prefilledcode_id=prefilledcode_id
        )
