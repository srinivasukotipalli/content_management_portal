from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface

class RoughSolutionDeletionInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def rough_solution_deletion(self,question_id:int,rough_solution_id:int):
        self.storage.rough_solution_deletion(
            question_id=question_id,
            rough_solution_id=rough_solution_id
        )
