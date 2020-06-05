import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec

from content_management_portal.interactors. \
    coding_questions_interactor import CodingQuestionsInteractor
from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
        coding_questions_presenter_interface import PresenterInterface



class TestCodingQuestionInteractor:

    def test_coding_questions_interactor(self, total_questions_dtos_list):
        # Arrange
        offset = 1
        limit = 2
        total_coding_questions = 1
        mock_response = {
                          "total_coding_questions": 1,
                          "question_details": [
                            {
                              "question_id": 1,
                              "short_title": "string",
                              "roughsolution": True,
                              "testcase": True,
                              "prefilledcode": True,
                              "solutionapproach": True,
                              "cleansolution": True,
                              "hint": True
                            }
                          ]
                        }

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = CodingQuestionsInteractor(storage=storage, \
                presenter=presenter)

        storage.get_question_details.return_value = (total_questions_dtos_list, \
                                                total_coding_questions)
        presenter.get_response_for_all_the_questions.return_value = mock_response

        # Act
        response = interactor.homepage_coding_questions(
                offset=offset,limit=limit
                )

        # Assert
        presenter.get_response_for_all_the_questions.assert_called_once_with(
                total_questions_dtos_list=total_questions_dtos_list,
                total_coding_questions=total_coding_questions)
        storage.get_question_details.assert_called_once_with(offset=offset,limit=limit)
        assert mock_response == response
