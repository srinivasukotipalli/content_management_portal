from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors. \
    presenters.get_question_presenter_interface import PresenterInterface
from content_management_portal.exceptions.exceptions import InvalidQuestionId


class GetQuestionInteractor:

    def __init__(self, storage: StorageInterface,
                    presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_question(self, question_id:int):

        try:
            self.storage.validate_question_id(question_id=question_id)
        except InvalidQuestionId:
            self.presenter.raise_invalid_question_exception()

        question_dto, list_of_roughsolution_dtos,list_of_testcase_dtos, \
            list_of_prefilledcode_dtos, solutionapproach_dto, \
                list_of_cleansolution_dtos, list_of_hint_dtos = \
                    self.storage.get_question(question_id=question_id)

        Question_complete_details_dict = \
                    self.presenter.get_question_dto_response(
                            question_dto, 
                            list_of_roughsolution_dtos,
                            list_of_testcase_dtos,
                            list_of_prefilledcode_dtos,
                            solutionapproach_dto,
                            list_of_cleansolution_dtos,
                            list_of_hint_dtos
                        )
        return Question_complete_details_dict