import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec

from content_management_portal.interactors. \
    get_question_interactor import GetQuestionInteractor
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
        get_question_presenter_interface import PresenterInterface


class TestGetQuestionInteractor:

    def test_get_coding_questions_interactor(self,
                                questiondto,
                                roughsolutioniddto,
                                testcasedto,
                                prefilledcodeiddto,
                                solutionapproachdto,
                                cleansolutiondto,
                                hintiddto
                                ):
        # Arrange
        question_dto = [questiondto]
        list_of_roughsolution_dtos = [roughsolutioniddto]
        list_of_testcase_dtos = [testcasedto]
        list_of_prefilledcode_dtos = [prefilledcodeiddto]
        solutionapproach_dto = solutionapproachdto
        list_of_cleansolution_dtos = [cleansolutiondto]
        list_of_hint_dtos = [hintiddto]

        question_id = 1
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = GetQuestionInteractor(storage=storage, presenter=presenter)

        storage.get_question.return_value = \
                                (
                                    question_dto,
                                    list_of_roughsolution_dtos,
                                    list_of_testcase_dtos,
                                    list_of_prefilledcode_dtos,
                                    solutionapproach_dto,
                                    list_of_cleansolution_dtos,
                                    list_of_hint_dtos
                                )

        mock_response = {
                          "question_details": {
                            "question_id": 1,
                            "short_title": "even",
                            "problem_description": {
                              "content_type": "HTML",
                              "content": "helloworld"
                            }
                          },
                          "roughsolutions": [
                            {
                              "roughsolution_id": 1,
                              "code_type": "PYTHON",
                              "code": "string",
                              "filename": "string"
                            }
                          ],
                          "testcases": [
                            {
                              "testcase_id": 1,
                              "input": "string",
                              "output": "string",
                              "is_hidden": True,
                              "score": 1,
                              "order_id": 1
                            }
                          ],
                          "prefilledcodes": [
                            {
                              "prefilledcode_id": 1,
                              "code_type": "PYTHON",
                              "code": "string",
                              "filename": "string"
                            }
                          ],
                          "solutionapproaches": {
                            "solutionapproach_id": 1,
                            "title": "string",
                            "description_content_type": "HTML",
                            "description_content": "string",
                            "complexity_analysis_content_type": "HTML",
                            "complexity_analysis_content": "string"
                          },
                          "cleansolutions": [
                            {
                              "cleansolution_id": 1,
                              "code_type": "PYTHON",
                              "code": "string",
                              "filename": "string"
                            }
                          ],
                          "hints": [
                            {
                              "hint_id": 1,
                              "title": "string",
                              "content_type": "HTML",
                              "content": "string",
                              "order_id": 1
                            }
                          ]
                        }
        
        presenter.get_question_dto_response.return_value = mock_response

        # Act
        response = interactor.get_question(question_id=question_id)
    
        # Assert
        storage.get_question.assert_called_once_with(question_id=question_id)
        presenter.get_question_dto_response.assert_called_once_with(
                            question_dto, 
                            list_of_roughsolution_dtos,
                            list_of_testcase_dtos,
                            list_of_prefilledcode_dtos,
                            solutionapproach_dto,
                            list_of_cleansolution_dtos,
                            list_of_hint_dtos
                        ) 
        
        assert mock_response == response
