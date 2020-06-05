import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from typing import List
from content_management_portal.interactors. \
    swap_hint_orders_interactor import \
    SwapHintInteractor
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
    swap_hints_presenter_interface import PresenterInterface


class TestSwapHintsInteractor:

    def test_swap_hint_interactor(self, swap_hint_dto):

        # Arrange
        
        swap_dto = swap_hint_dto
        swap_hint_details = \
            {
                "first_hint": {
                "hint_id": 0,
                "hint_number": 0
                },
                "second_hint": {
                "hint_id": 0,
                "hint_number": 0
                }
            }
        question_id = 1
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        interactor = SwapHintInteractor(storage=storage, \
                        presenter=presenter)


        # Act
        interactor.swap_hint_numbers(
                                question_id=question_id,
                                swap_hint_details=swap_hint_details
                                )


        # Assert
        storage.validate_question_id.assert_called_once_with(question_id=question_id)
        storage.validate_hint_ids.assert_called_once_with(
                first_hint_id=0,
                second_hint_id=0
                )
        storage.validate_question_hints_match( \
                question_id=question_id,
                first_hint_id=0,
                second_hint_id=0
                )
        storage.swap_hint_numbers_for_hints( \
                                            self, swap_dto=swap_dto)
