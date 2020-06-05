from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos import TestCaseDto

class PresenterInterface(ABC):
    
    @abstractmethod
    def raise_invalid_question_exception(self):
        pass

    @abstractmethod
    def raise_invalid_testcase_exception(self):
        pass
    
    @abstractmethod
    def raise_invalid_testcase_for_question_exception(self):
        pass

    @abstractmethod
    def get_response_for_testcase(self,testcase_dto: TestCaseDto):
                pass
