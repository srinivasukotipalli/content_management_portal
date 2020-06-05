from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos \
    import QuestionDto


class PresenterInterface(ABC):

    @abstractmethod
    def get_question_dto_response(self,
        questiondto: QuestionDto):
        pass

    @abstractmethod
    def raise_invalid_question_exception(self):
        pass
