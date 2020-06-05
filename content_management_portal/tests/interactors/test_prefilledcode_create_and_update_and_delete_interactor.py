import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from typing import List
from content_management_portal.interactors. \
    prefilledcode_create_or_update_interactor import \
    PrefilledCodeCreateOrUpdateInteractor
from content_management_portal.interactors. \
    prefilledcode_delete_interactor import PrefilledCodeDeletionInteractor
from content_management_portal.constants.enums import TextType, CodeLanguage
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
      prefilledcode_presenter_interface import PresenterInterface


class TestPrefilledCodeInteractor:

    def test_prefilledcode_create_or_update_interactor(self, \
              prefilledcodeiddto,prefilledcodedto):
        
        # Arrange
        question_id=1
        list_of_prefilledcode_ids = [1]
        question_prefilledcode_list = [
                          {
                              "prefilledcode_id": 1,
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
                              "prefilledcode_id": 1,
                              "code_type": CodeLanguage.python.value,
                              "code": "string",
                              "filename": "string"
                          }
                        ]
        
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = PrefilledCodeCreateOrUpdateInteractor(storage=storage, \
                        presenter=presenter)
        
        list_of_prefilledcode_dto = [
            prefilledcodedto
        ]
        

        storage.updation_and_creation_of_prefilledcodes.return_value = \
                list_of_prefilledcode_dto
        presenter.get_response_for_list_of_prefilledcode_dtos.return_value = mock_response

        # Act
        response = interactor.prefilledcode_create_or_update(
                question_id=question_id,
                question_prefilledcode_list=question_prefilledcode_list
                )

        # Assert
        assert mock_response == response
        storage.validate_question_id.assert_called_once_with(question_id=question_id)
        storage.validate_prefilledcode_ids.assert_called_once_with( \
                    list_of_prefilledcode_ids=list_of_prefilledcode_ids)
        storage.validate_question_prefilledcode_match.assert_called_once_with( \
                        question_id=question_id,
                        list_of_prefilledcode_ids=list_of_prefilledcode_ids
                        )
        storage.updation_and_creation_of_prefilledcodes.assert_called_once_with(
                        question_id=question_id,
                        updated_prefilledcode_dtos=[prefilledcodeiddto],
                        created_prefilledcode_dtos=[prefilledcodedto]
          )

    def test_prefilledcode_deletion_Interactor(self):
        # Arrange
        question_id = 1
        prefilledcode_id = 1

        storage = create_autospec(StorageInterface)

        interactor = PrefilledCodeDeletionInteractor(storage=storage)

        # Act
        interactor.prefilledcode_deletion(question_id=question_id, \
                        prefilledcode_id=prefilledcode_id)

        # Assert
        storage.prefilledcode_deletion.assert_called_once_with( \
        		question_id=question_id,
        		prefilledcode_id=prefilledcode_id)
