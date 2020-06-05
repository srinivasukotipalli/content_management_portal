from abc import ABC
from abc import abstractmethod
from typing import List
from content_management_portal.interactors.storages.dtos \
    import QuestionDetailsDto
from content_management_portal.interactors.storages.dtos \
    import QuestionDetailsDto


class PresenterInterface:
    
    @abstractmethod
    def raise_is_invalid_offset_value(self):
        pass

    @abstractmethod
    def raise_is_invalid_limit_value(self):
        pass

    @abstractmethod
    def get_response_for_all_the_questions(self, \
                    total_questions_dtos_list: List[QuestionDetailsDto], \
                    total_coding_questions: int):
        pass


