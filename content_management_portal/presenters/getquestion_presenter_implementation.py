from content_management_portal.interactors. \
    presenters.get_question_presenter_interface import PresenterInterface
from content_management_portal.constants.exception_messages \
    import INVALID_QUESTION_ID
from django_swagger_utils.drf_server.exceptions import NotFound


class PresenterImplementation(PresenterInterface):

    def raise_invalid_question_exception(self):
        raise NotFound(*INVALID_QUESTION_ID)

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
            questiondetails_dict = {
                "question_details": {
                    "question_id": question_dto.question_id,
                    "short_title": question_dto.short_title,
                    "problem_description": {
                        "content_type": question_dto.content_type,
                        "content": question_dto.content
                    }
                },

                "roughsolutions": \
                        self._roughsolutions_list(list_of_roughsolution_dtos),

                "testcases": \
                        self._testcases_list(list_of_testcase_dtos),

                "prefilledcodes": \
                        self._prefilledcodes_list(list_of_prefilledcode_dtos),

                "solutionapproaches": \
                        self._solutionapproach(solutionapproach_dto),

                "cleansolutions": \
                        self._cleansolutions_list(list_of_cleansolution_dtos),

                "hints": \
                        self._hints_list(list_of_hint_dtos),
            }

            return questiondetails_dict



    @staticmethod
    def _roughsolutions_list(list_of_roughsolution_dtos):
        list_of_roughsolutions = \
        [
            {
              "roughsolution_id": dto.roughsolution_id,
              "code_type": dto.code_type,
              "code": dto.code,
              "filename": dto.filename
            }
            for dto in list_of_roughsolution_dtos
        ]

        return list_of_roughsolutions


    @staticmethod
    def _testcases_list(list_of_testcase_dtos):
        list_of_testcases = \
        [
            {
              "testcase_id": dto.testcase_id,
              "input": dto.input,
              "output": dto.output,
              "is_hidden": dto.is_hidden,
              "score": dto.score,
              "order_id": dto.order_id
            }
            for dto in list_of_testcase_dtos
        ]

        return list_of_testcases

    @staticmethod
    def _prefilledcodes_list(list_of_prefilledcode_dtos):
        list_of_prefilledcode_dict = \
            [
                {
                    "prefilledcode_id": dto.prefilledcode_id,
                    "code_type": dto.code_type,
                    "code": dto.code,
                    "filename": dto.filename
                }
                for dto in list_of_prefilledcode_dtos
            ]

        return list_of_prefilledcode_dict

    @staticmethod
    def _cleansolutions_list(list_of_cleansolution_dtos):
        list_of_cleansolutions_dicts = \
            [
                {
                    "cleansolution_id": dto.cleansolution_id,
                    "code_type": dto.code_type,
                    "code": dto.code,
                    "filename": dto.filename
                }
                for dto in list_of_cleansolution_dtos
            ]

        return list_of_cleansolutions_dicts

    @staticmethod
    def _solutionapproach(obj):
        if obj == None:
            return []
        else:
            solutionapproach_dict = \
                {
                    "solutionapproach_id": obj.solutionapproach_id,
                    "title": obj.title,
                    "description_content_type": obj.description_content_type,
                    "description_content": obj.description_content,
                    "complexity_analysis_content_type": \
                                    obj.complexity_analysis_content_type,
                    "complexity_analysis_content": obj.complexity_analysis_content
                }
            return solutionapproach_dict

    @staticmethod
    def _hints_list(list_of_hint_dtos):
        list_of_hint_dicts = \
            [
                {
                    "hint_id": dto.hint_id,
                    "title": dto.title,
                    "content_type": dto.content_type,
                    "content": dto.content,
                    "order_id": dto.order_id,
                }
                for dto in list_of_hint_dtos
            ]

        return list_of_hint_dicts

