import pytest

from content_management_portal.models import Question, Hint
from content_management_portal.storages.swap_hints_for_testcase_numbers import \
    SwapHintStorageImplementation
from content_management_portal.exceptions import (
    InvalidHintId,
    InvalidHintForQuestion,
    InvalidQuestionId
    )


class TestSwapHint:

    @pytest.mark.django_db
    def test_swap_hints_order(self, create_question, swap_hint_dto):
    
        # Arrange
        question_id = 1
        storage = SwapHintStorageImplementation()
        
        # Act
        storage.swap_hint_numbers_for_hints( \
                                            question_id=question_id,
                                            swap_dto=swap_hint_dto
                                        )
        hint_object = Hint.objects.get(id=1)
        
        # assert
        assert hint_object.order_id == 2



    @pytest.mark.django_db
    def test_validate_question_hints_match(self, create_hints):
    
        # Arrange

        storage = SwapHintStorageImplementation()
        
        # Act
        response = storage.validate_question_hints_match( \
                                            question_id=1,
                                            first_hint_id=1,
                                            second_hint_id=2
                                        )

        # Assert
        assert response == None
    
    @pytest.mark.django_db
    def test_validate_question_hints_match_raises_error(self, create_hints):
    
        # Arrange

        storage = SwapHintStorageImplementation()
        
        # Assert
        
        with pytest.raises(InvalidHintForQuestion):
            storage.validate_question_hints_match( \
                                            question_id=1,
                                            first_hint_id=1,
                                            second_hint_id=1)
                        

    
    @pytest.mark.django_db
    def test_validate_hint_ids(self, create_hints):
    
        # Arrange

        storage = SwapHintStorageImplementation()
        
        # Act
        response = storage.validate_hint_ids(
                                            first_hint_id=1,
                                            second_hint_id=2)
                        
        
        # Assert 
        assert response == None
    
    
    @pytest.mark.django_db
    def test_validate_question_hints_raises_error(self, create_testcases):
    
        # Arrange

        storage = SwapHintStorageImplementation()
        
        # Assert
        with pytest.raises(InvalidHintId):
            storage.validate_hint_ids( \
                                            first_hint_id=1,
                                            second_hint_id=1)

    
    @pytest.mark.django_db
    def test_validate_question_id(self, create_question):
    
        # Arrange
        question_id = 1
        expected_output = True
        storage = SwapHintStorageImplementation()
        storage.validate_question_id(question_id=question_id)
        
        # Act
        is_question_exists = Question.objects.filter(id=question_id).exists()
        
        # Assert
        assert expected_output == is_question_exists
    
    
    @pytest.mark.django_db
    def test_validate_invalid_question_id(self, create_question):
    
        # Arrange
        question_id = 2
        storage = SwapHintStorageImplementation()
        
        # Assert
        with pytest.raises(InvalidQuestionId):
            storage.validate_question_id(question_id=question_id)
