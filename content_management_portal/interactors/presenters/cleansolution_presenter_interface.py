from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos import CleanSolutionDto


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_question_exception(self):
        pass

    @abstractmethod
    def raise_invalid_cleansolution_exception(self):
        pass

    @abstractmethod
    def raise_invalid_cleansolution_for_question_exception(self):
        pass

    @abstractmethod
    def get_response_for_list_of_cleansolution_dtos(self, \
            list_of_cleansolution_dtos=List[CleanSolutionDto]):
        pass
