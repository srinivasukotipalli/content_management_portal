from content_management_portal.interactors.presenters. \
    coding_questions_presenter_interface import PresenterInterface
from content_management_portal.constants.exception_messages \
    import (
            INVALID_QUESTION_ID,
            INVALID_OFFSET_VALUE,
            INVALID_LIMIT_VALUE
           )
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from typing import List
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,QuestionDetailsDto

class PresenterImplementation(PresenterInterface):

    def get_response_for_all_the_questions(self, \
                total_questions_dtos_list: List[QuestionDetailsDto], \
                    total_coding_questions: int):

        question_details_dictionary = {
            "total_coding_questions" : total_coding_questions
        }

        question_details_dictionary["question_details"] = \
            self._convert_question_dto_to_get_response(
                total_questions_dtos_list)
        return question_details_dictionary

    @staticmethod
    def _convert_question_dto_to_get_response(total_questions_dtos_list):

        questions_list = []

        for dto in total_questions_dtos_list:
            question_dictionary = {}
            question_dictionary['question_id'] = dto.question_id
            question_dictionary['short_title'] = dto.short_title
            question_dictionary['roughsolution'] = dto.roughsolution
            question_dictionary['testcase'] = dto.testcase
            question_dictionary['prefilledcode'] = dto.prefilledcode
            question_dictionary['solutionapproach'] = dto.solutionapproach
            question_dictionary['cleansolution'] = dto.cleansolution
            question_dictionary['hint'] = dto.hint

            questions_list.append(question_dictionary)

        return questions_list


    def raise_is_invalid_offset_value(self):
        raise BadRequest(*INVALID_OFFSET_VALUE)

    def raise_is_invalid_limit_value(self):
        raise BadRequest(*INVALID_LIMIT_VALUE)
