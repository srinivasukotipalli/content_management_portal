import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from typing import List
from content_management_portal.interactors. \
    testcase_create_or_update_interactor import \
    CaseCreateOrUpdateInteractor
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
    testcase_presenter_interface import PresenterInterface
from content_management_portal.interactors. \
    testcase_deletion_interactor import \
    CaseDeletionInteractor

class TestTestCaseInteractor:

    def test_testcase_creation_interactor(self, testcasedto, testcaseiddto):

        # Arrange
        question_id = 1
        testcase_details = {
                    "order_id": 1,
                    "input": "string",
                    "output": "string",
                    "is_hidden": True,
                    "score": 1
                    }

        mock_response = {
                            "order_id": 1,
                            "testcase_id": 1,
                            "input": "string",
                            "output": "string",
                            "is_hidden": True,
                            "score": 1
                          }

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = CaseCreateOrUpdateInteractor(storage=storage, \
                        presenter=presenter)

        storage.testcase_creation.return_value = testcaseiddto
        presenter.get_response_for_testcase.return_value = mock_response

        # Act
        response = interactor.testcase_create_or_update(
                                question_id=question_id,
                                testcase_details=testcase_details
                                )


        # Assert
        assert mock_response == response
        storage.validate_question_id.assert_called_once_with(question_id=question_id)
        storage.testcase_creation.assert_called_once_with(
                        question_id=question_id,
                        created_testcase_dto=testcasedto,
          )
        presenter.get_response_for_testcase(testcase_dto=testcaseiddto)

    def test_testcase_updation_interactor(self, testcaseiddto):

        # Arrange
        question_id = 1
        testcase_id = 1
        testcase_details = {
                    "order_id": 1,
                    "testcase_id": 1,
                    "input": "string",
                    "output": "string",
                    "is_hidden": True,
                    "score": 1
                    }

        mock_response = {
                            "order_id": 1,
                            "testcase_id": 1,
                            "input": "string",
                            "output": "string",
                            "is_hidden": True,
                            "score": 1
                          }

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = CaseCreateOrUpdateInteractor(storage=storage, \
                        presenter=presenter)

        storage.testcase_updation.return_value = testcaseiddto
        presenter.get_response_for_testcase.return_value = mock_response

        # Act
        response = interactor.testcase_create_or_update(
                                question_id=question_id,
                                testcase_details=testcase_details
                                )
                

        # Assert
        assert mock_response == response
        storage.validate_question_id.assert_called_once_with(question_id=question_id)
        storage.validate_testcase_id.assert_called_once_with(
                    testcase_id=testcase_id)
        storage.validate_question_testcase_match.assert_called_once_with( \
                        question_id=question_id,
                        testcase_id=testcase_id
                        )
        storage.testcase_updation.assert_called_once_with(
                        question_id=question_id,
                        updated_testcase_dto=testcaseiddto,
          )
        presenter.get_response_for_testcase(testcase_dto=testcaseiddto)


    def test_testcase_deletion_Interactor(self):
        # Arrange
        question_id = 1
        testcase_id = 1

        storage = create_autospec(StorageInterface)

        interactor = CaseDeletionInteractor(storage=storage)

        # Act
        interactor.testcase_deletion( \
                        question_id=question_id,
                        testcase_id=testcase_id)

        # Assert
        storage.testcase_deletion.assert_called_once_with( \
                        question_id=question_id,
                        testcase_id=testcase_id)
