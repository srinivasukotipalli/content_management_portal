from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos import RoughSolutionDto

class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_rough_solution_exception(self):
        pass
    
    @abstractmethod
    def raise_invalid_rough_solution_for_question_exception(self):
        pass

    @abstractmethod
    def get_response_for_list_of_rough_solutions_dtos( \
            self,list_of_rough_solution_dtos:List[RoughSolutionDto]):
                pass

    @abstractmethod
    def raise_invalid_question_exception(self):
        pass
