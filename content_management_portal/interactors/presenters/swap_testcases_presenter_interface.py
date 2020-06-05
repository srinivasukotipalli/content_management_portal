from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos \
    import SwapTestCaseDto, QuestionDto


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
