import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from typing import List
from content_management_portal.interactors. \
    hint_create_or_update_interactor import \
    HintCreateOrUpdateInteractor
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
    hint_presenter_interface import PresenterInterface
from content_management_portal.interactors. \
    hint_deletion_interactor import \
    HintDeletionInteractor
from content_management_portal.constants.enums import TextType

class TestHintInteractor:

    def test_hint_creation_interactor(self, hintdto, hintiddto):

        # Arrange
        question_id = 1
        hint_details = {
                        "title": "string",
                        "content_type": TextType.html.value,
                        "content": "string",
                        "order_id": 1
                        }

        mock_response = {
                            "hint_id": 1,
                            "title": "string",
                            "content_type": TextType.html.value,
                            "content": "string",
                            "order_id": 1
                          }

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = HintCreateOrUpdateInteractor(storage=storage, \
                        presenter=presenter)

        storage.hint_creation.return_value = hintiddto
        presenter.get_response_for_hint.return_value = mock_response

        # Act
        response = interactor.hint_create_or_update(
                                question_id=question_id,
                                hint_details=hint_details
                                )


        # Assert
        assert mock_response == response
        storage.validate_question_id.assert_called_once_with( \
                                                question_id=question_id)
        storage.hint_creation.assert_called_once_with(
                        question_id=question_id,
                        created_hint_dto=hintdto,
          )
        presenter.get_response_for_hint(hint_dto=hintiddto)

    def test_hint_updation_interactor(self, hintiddto):

        # Arrange
        question_id = 1
        hint_id = 1
        hint_details = {
                            "hint_id": 1,
                            "title": "string",
                            "content_type": TextType.html.value,
                            "content": "string",
                            "order_id": 1
                        }

        mock_response = {
                            "hint_id": 1,
                            "title": "string",
                            "content_type": TextType.html.value,
                            "content": "string",
                            "order_id": 1
                        }

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = HintCreateOrUpdateInteractor(storage=storage, \
                        presenter=presenter)

        storage.hint_updation.return_value = hintiddto
        presenter.get_response_for_hint.return_value = mock_response

        # Act
        response = interactor.hint_create_or_update(
                                question_id=question_id,
                                hint_details=hint_details
                                )
                

        # Assert
        assert mock_response == response
        storage.validate_question_id.assert_called_once_with(question_id=question_id)
        storage.validate_hint_id.assert_called_once_with(
                    hint_id=hint_id)
        storage.validate_question_hint_match.assert_called_once_with( \
                        question_id=question_id,
                        hint_id=hint_id
                        )
        storage.hint_updation.assert_called_once_with(
                        question_id=question_id,
                        updated_hint_dto=hintiddto,
          )
        presenter.get_response_for_hint(hint_dto=hintiddto)


    def test_hint_deletion_Interactor(self):
        # Arrange
        question_id = 1
        hint_id = 1

        storage = create_autospec(StorageInterface)

        interactor = HintDeletionInteractor(storage=storage)

        # Act
        interactor.hint_deletion( \
                        question_id=question_id,
                        hint_id=hint_id)

        # Assert
        storage.hint_deletion.assert_called_once_with( \
                        question_id=question_id,
                        hint_id=hint_id)
