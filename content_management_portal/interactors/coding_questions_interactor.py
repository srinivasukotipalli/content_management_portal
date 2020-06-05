from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
    coding_questions_presenter_interface import PresenterInterface


class CodingQuestionsInteractor:


    def __init__(self, storage: StorageInterface, \
                    presenter: PresenterInterface):
                        self.storage = storage
                        self.presenter = presenter

    def homepage_coding_questions(self,offset: int,limit: int):

        self._is_invalid_offset_value(offset=offset)
        self._is_invalid_limit_value(limit=limit)



        total_questions_dtos_list, total_coding_questions = \
                self.storage.get_question_details(offset=offset, limit=limit)

        list_of_total_questions = \
                    self.presenter.get_response_for_all_the_questions( \
                            total_questions_dtos_list=total_questions_dtos_list,
                            total_coding_questions=total_coding_questions
                            )

        return list_of_total_questions

    def _is_invalid_offset_value(self, offset: int):
        valid_offset = offset>=0
        if not valid_offset:
            self.presenter.raise_is_invalid_offset_value()

    def _is_invalid_limit_value(self, limit: int):
        valid_limit = limit>0
        if not valid_limit:
            self.presenter.raise_is_invalid_limit_value()
