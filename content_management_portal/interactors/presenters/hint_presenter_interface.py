from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos import HintDto

class PresenterInterface(ABC):
    
    @abstractmethod
    def raise_invalid_question_exception(self):
        pass

    @abstractmethod
    def raise_invalid_hint_exception(self):
        pass
    
    @abstractmethod
    def raise_invalid_hint_for_question_exception(self):
        pass

    @abstractmethod
    def get_response_for_hint(self,hint_dto: HintDto):
                pass
