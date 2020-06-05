import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from typing import List
from content_management_portal.interactors. \
    swap_testcase_orders_interactor import \
    SwapCasesInteractor
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
    swap_testcases_presenter_interface import PresenterInterface


class TestSwapTestCaseInteractor:

    def test_swap_testcase_interactor(self, swap_testcase_dto):

        # Arrange
        
        swap_dto = swap_testcase_dto
        swap_testcase_details = \
            {
              "first_testcase": {
                "testcase_id": 0,
                "testcase_number": 0
              },
              "second_testcase": {
                "testcase_id": 0,
                "testcase_number": 0
              }
            }
        question_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = SwapCasesInteractor(storage=storage, \
                        presenter=presenter)


        # Act
        interactor.swap_testcase_numbers(
                                question_id=question_id,
                                swap_testcase_details=swap_testcase_details
                                )


        # Assert
        storage.validate_question_id.assert_called_once_with(question_id=question_id)
        storage.validate_testcase_ids.assert_called_once_with(
                first_testcase_id=0,
                second_testcase_id=0
                )
        storage.validate_question_testcases_match( \
                question_id=question_id,
                first_testcase_id=0,
                second_testcase_id=0
                )
        storage.swap_testcase_numbers_for_testcases( \
                                            self, swap_dto=swap_dto)
