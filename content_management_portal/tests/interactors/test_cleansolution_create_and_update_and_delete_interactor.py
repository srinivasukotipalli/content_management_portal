import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from typing import List
from content_management_portal.interactors. \
    cleansolution_create_or_update_interactor import \
    CleanSolutionCreateOrUpdateInteractor
from content_management_portal.interactors. \
    cleansolution_deletion_interactor import CleanSolutionDeletionInteractor
from content_management_portal.constants.enums import TextType, CodeLanguage
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
      cleansolution_presenter_interface import PresenterInterface


class TestCleanSolutionInteractor:

    def test_cleansolution_create_or_update_interactor(self, \
              cleansolutioniddto, cleansolutiondto):
        
        # Arrange
        question_id=1
        list_of_cleansolution_ids = [1]
        question_cleansolution_list = [
                          {
                              "cleansolution_id": 1,
                              "code_type": CodeLanguage.python.value,
                              "code": "string",
                              "filename": "string"
                          },
                          {
                              "code_type": CodeLanguage.python.value,
                              "code": "string",
                              "filename": "string"
                          }
                        ]
        
        mock_response = [
                          {
                              "cleansolution_id": 1,
                              "code_type": CodeLanguage.python.value,
                              "code": "string",
                              "filename": "string"
                          }
                        ]
        
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = CleanSolutionCreateOrUpdateInteractor(storage=storage, \
                        presenter=presenter)
        
        list_of_cleansolution_dto = [
            cleansolutiondto
        ]
        

        storage.updation_and_creation_of_cleansolutions.return_value = \
                list_of_cleansolution_dto
        presenter.get_response_for_list_of_cleansolution_dtos.return_value = mock_response

        # Act
        response = interactor.cleansolution_create_or_update(
                question_id=question_id,
                question_cleansolution_list=question_cleansolution_list
                )

        # Assert
        assert mock_response == response
        storage.validate_question_id.assert_called_once_with(question_id=question_id)
        storage.validate_cleansolution_ids.assert_called_once_with( \
                    list_of_cleansolution_ids=list_of_cleansolution_ids)
        storage.validate_question_cleansolution_match.assert_called_once_with( \
                        question_id=question_id,
                        list_of_cleansolution_ids=list_of_cleansolution_ids
                        )
        storage.updation_and_creation_of_cleansolutions.assert_called_once_with(
                        question_id=question_id,
                        updated_cleansolution_dtos=[cleansolutioniddto],
                        created_cleansolution_dtos=[cleansolutiondto]
          )

    def test_cleansolution_deletion_Interactor(self):
        # Arrange
        question_id = 1
        cleansolution_id = 1

        storage = create_autospec(StorageInterface)

        interactor = CleanSolutionDeletionInteractor(storage=storage)

        # Act
        interactor.cleansolution_deletion(question_id=question_id, \
                        cleansolution_id=cleansolution_id)

        # Assert
        storage.cleansolution_deletion.assert_called_once_with( \
        		question_id=question_id,
        		cleansolution_id=cleansolution_id)
