from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface

class CleanSolutionDeletionInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def cleansolution_deletion(self,question_id:int,cleansolution_id:int):
        self.storage.cleansolution_deletion(
            question_id=question_id,
            cleansolution_id=cleansolution_id
        )
