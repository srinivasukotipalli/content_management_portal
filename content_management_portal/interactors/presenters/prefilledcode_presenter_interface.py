from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos import PrefilledCodeDto


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_question_exception(self):
        pass

    @abstractmethod
    def raise_invalid_prefilledcode_exception(self):
        pass

    @abstractmethod
    def raise_invalid_prefilledcode_for_question_exception(self):
        pass

    @abstractmethod
    def get_response_for_list_of_prefilledcode_dtos(self, \
            list_of_prefilledcode_dtos=List[PrefilledCodeDto]):
        pass
