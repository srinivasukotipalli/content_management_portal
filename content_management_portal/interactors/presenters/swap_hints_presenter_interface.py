from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos \
    import SwapHintDto, QuestionDto


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
