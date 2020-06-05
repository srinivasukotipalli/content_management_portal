from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface

class CaseDeletionInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def testcase_deletion(self,question_id:int, testcase_id:int):
        self.storage.testcase_deletion( \
                        question_id=question_id,
                        testcase_id=testcase_id
                        )
