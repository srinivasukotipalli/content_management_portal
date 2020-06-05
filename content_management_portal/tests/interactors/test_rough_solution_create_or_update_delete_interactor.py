import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from typing import List
from content_management_portal.interactors. \
    rough_solution_create_or_update_interactor import \
    RoughSolutionCreateOrUpdateInteractor
from content_management_portal.constants.enums import TextType, CodeLanguage
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
    roughsolution_presenter_interface import PresenterInterface
from content_management_portal.interactors. \
    rough_solution_deletion_interactor import \
    RoughSolutionDeletionInteractor

class TestRoughSolutionInteractor:

    def test_rough_solution_create_or_update_interactor(self, \
              roughsolutioniddto,roughsolutiondto):
        
        # Arrange
        question_id=1
        list_of_rough_solutions_ids = [1]
        question_rough_solutions_list = [
                          {
                            "roughsolution_id": 1,
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
                            "roughsolution_id": 1,
                              "code_type": CodeLanguage.python.value,
                              "code": "string",
                              "filename": "string"
                          }
                        ]
        
        
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = RoughSolutionCreateOrUpdateInteractor(storage=storage, \
                        presenter=presenter)
        
        list_of_rough_solutions_dto = [
            roughsolutiondto
        ]
        storage.updation_and_creation_of_rough_solutions.return_value = \
                list_of_rough_solutions_dto
        presenter.get_response_for_list_of_rough_solutions_dtos.return_value = mock_response
        

        
        # Act
        response = interactor.rough_solution_create_or_update(
                question_id=question_id,
                question_rough_solutions_list=question_rough_solutions_list
                )

        # Assert
        assert mock_response == response
        storage.validate_question_id.assert_called_once_with(question_id=question_id)
        storage.validate_rough_solution_ids.assert_called_once_with(
                    list_of_rough_solutions_ids=list_of_rough_solutions_ids)
        storage.validate_question_roughsolutions_match.assert_called_once_with( \
                        question_id=question_id,
                        list_of_rough_solutions_ids=list_of_rough_solutions_ids
                        )
        storage.updation_and_creation_of_rough_solutions.assert_called_once_with(
                        question_id=question_id,
                        updated_rough_solutions_dtos=[roughsolutioniddto],
                        created_rough_solutions_dtos=[roughsolutiondto]
          )
        
    def test_rough_solution_deletion_Interactor(self):
        # Arrange
        question_id = 1
        rough_solution_id = 1

        storage = create_autospec(StorageInterface)

        interactor = RoughSolutionDeletionInteractor(storage=storage)

        # Act
        interactor.rough_solution_deletion(question_id=question_id, \
                        rough_solution_id=rough_solution_id)

        # Assert
        storage.rough_solution_deletion.assert_called_once_with( \
        		question_id=question_id,
        		rough_solution_id=rough_solution_id)


