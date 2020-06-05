from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos \
    import SolutionApproachDto

class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_question_exception(self):
        pass

    @abstractmethod
    def raise_invalid_solutionapproach_exception(self):
        pass

    @abstractmethod
    def raise_invalid_solutionapproach_for_question_exception(self):
        pass

    @abstractmethod
    def get_response_for_solutionapproach(self, \
                            solutionapproach_dto: SolutionApproachDto):
                pass
