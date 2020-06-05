from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface

class SolutionapproachDeletionInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def solutionapproach_deletion(self,question_id:int, solutionapproach_id:int):
        self.storage.solutionapproach_deletion( \
                        question_id=question_id,
                        solutionapproach_id=solutionapproach_id
                        )
