import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from typing import List
from content_management_portal.interactors. \
    solutionapproach_create_or_update_interactor import \
    SolutionapproachCreateOrUpdateInteractor
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
    solutionapproach_presenter_interface import PresenterInterface
from content_management_portal.interactors. \
    solutionapproach_deletion_interactor import \
    SolutionapproachDeletionInteractor
from content_management_portal.constants.enums import TextType

class TestSolutionApproachInteractor:

    def test_solutionapproach_creation_interactor(self, \
                        solutionapproachdto, solutionapproachiddto):

        # Arrange
        question_id = 1
        solutionapproach_details = {
                        "title": "string",
                        "description_content_type": TextType.html.value,
                        "description_content": "string",
                        "complexity_analysis_content_type": TextType.html.value,
                        "complexity_analysis_content": "string",
                        "question_id": question_id
                        }

        mock_response = {
                        "solutionapproach_id": 1,
                        "title": "string",
                        "description_content_type": TextType.html.value,
                        "description_content": "string",
                        "complexity_analysis_content_type": TextType.html.value,
                        "complexity_analysis_content": "string",
                        "question_id": question_id
                        }

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = SolutionapproachCreateOrUpdateInteractor(storage=storage, \
                        presenter=presenter)

        storage.solutionapproach_creation.return_value = solutionapproachiddto
        presenter.get_response_for_solutionapproach.return_value = mock_response

        # Act
        response = interactor.solutionapproach_create_or_update(
                                question_id=question_id,
                                solutionapproach_details=solutionapproach_details
                                )

        # Assert
        assert mock_response == response
        storage.validate_question_id.assert_called_once_with( \
                                                question_id=question_id)
        storage.solutionapproach_creation.assert_called_once_with(
                        question_id=question_id,
                        created_solutionapproach_dto=solutionapproachdto,
          )
        presenter.get_response_for_solutionapproach( \
                            solutionapproach_dto=solutionapproachiddto)

    def test_solutionapproach_updation_interactor(self, solutionapproachiddto):

        # Arrange
        question_id = 1
        solutionapproach_id = 1
        solutionapproach_details = {
                        "solutionapproach_id": 1,
                        "title": "string",
                        "description_content_type": TextType.html.value,
                        "description_content": "string",
                        "complexity_analysis_content_type": TextType.html.value,
                        "complexity_analysis_content": "string"
                        }

        mock_response = {
                            "solutionapproach_id": 1,
                            "title": "string",
                            "description_content_type": TextType.html.value,
                            "description_content": "string",
                            "complexity_analysis_content_type": TextType.html.value,
                            "complexity_analysis_content": "string"
                        }

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = SolutionapproachCreateOrUpdateInteractor(storage=storage, \
                        presenter=presenter)

        storage.solutionapproach_updation.return_value = solutionapproachiddto
        presenter.get_response_for_solutionapproach.return_value = mock_response

        # Act
        response = interactor.solutionapproach_create_or_update(
                            question_id=question_id,
                            solutionapproach_details=solutionapproach_details
                            )
                

        # Assert
        assert mock_response == response
        storage.validate_question_id.assert_called_once_with(question_id=question_id)
        storage.validate_solutionapproach_id.assert_called_once_with(
                    solutionapproach_id=solutionapproach_id)
        storage.validate_question_solutionapproach_match. \
                                assert_called_once_with( \
                                    question_id=question_id,
                                    solutionapproach_id=solutionapproach_id
                                    )
        storage.solutionapproach_updation.assert_called_once_with(
                        question_id=question_id,
                        updated_solutionapproach_dto=solutionapproachiddto,
          )
        presenter.get_response_for_solutionapproach( \
                            solutionapproach_dto=solutionapproachiddto)


    def test_hint_deletion_Interactor(self):
        # Arrange
        question_id = 1
        solutionapproach_id = 1

        storage = create_autospec(StorageInterface)

        interactor = SolutionapproachDeletionInteractor(storage=storage)

        # Act
        interactor.solutionapproach_deletion( \
                        question_id=question_id,
                        solutionapproach_id=solutionapproach_id)

        # Assert
        storage.solutionapproach_deletion.assert_called_once_with( \
                        question_id=question_id,
                        solutionapproach_id=solutionapproach_id)
