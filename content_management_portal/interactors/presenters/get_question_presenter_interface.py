from abc import ABC
from abc import abstractmethod
from typing import List


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_question_exception(self):
        pass

    @abstractmethod
    def get_question_dto_response( \
        self,
        question_dto,
        list_of_roughsolution_dtos,
        list_of_testcase_dtos,
        list_of_prefilledcode_dtos,
        solutionapproach_dto,
        list_of_cleansolution_dtos,
        list_of_hint_dtos
        ):
            pass