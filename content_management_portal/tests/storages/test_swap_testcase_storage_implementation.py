import pytest

from content_management_portal.models import Question, Case
from content_management_portal.storages.swap_testcases_for_testcase_numbers import \
    SwapTestCaseStorageImplementation
from content_management_portal.exceptions import (
    InvalidTestCaseId,
    InvalidTestCaseForQuestion,
    InvalidQuestionId
    )


class TestTestcase:

    @pytest.mark.django_db
    def test_testcase_creation(self, create_question, swap_testcase_dto):
    
        # Arrange
        question_id = 1
        storage = SwapTestCaseStorageImplementation()
        
        # Act
        storage.swap_testcase_numbers_for_testcases( \
                                            question_id=question_id,
                                            swap_dto=swap_testcase_dto
                                        )
        test_case_object = Case.objects.get(id=1)
        
        # assert
        assert test_case_object.order_id == 2



    @pytest.mark.django_db
    def test_validate_question_testcases_match(self, create_testcases):
    
        # Arrange

        storage = SwapTestCaseStorageImplementation()
        
        # Act
        response = storage.validate_question_testcases_match( \
                                            question_id=1,
                                            first_testcase_id=1,
                                            second_testcase_id=2
                                        )

        # Assert
        assert response == None
    
    @pytest.mark.django_db
    def test_validate_question_testcases_match_raises_error(self, create_testcases):
    
        # Arrange

        storage = SwapTestCaseStorageImplementation()
        
        # Assert
        
        with pytest.raises(InvalidTestCaseForQuestion):
            storage.validate_question_testcases_match( \
                                            question_id=1,
                                            first_testcase_id=1,
                                            second_testcase_id=1)
                        

    
    @pytest.mark.django_db
    def test_validate_testcase_ids(self, create_testcases):
    
        # Arrange

        storage = SwapTestCaseStorageImplementation()
        
        # Act
        response = storage.validate_testcase_ids(
                                            first_testcase_id=1,
                                            second_testcase_id=2)
                        
        
        # Assert 
        assert response == None
    
    
    @pytest.mark.django_db
    def test_validate_question_testcases_raises_error(self, create_testcases):
    
        # Arrange

        storage = SwapTestCaseStorageImplementation()
        
        # Assert
        with pytest.raises(InvalidTestCaseId):
            storage.validate_testcase_ids( \
                                            first_testcase_id=1,
                                            second_testcase_id=1)

    
    @pytest.mark.django_db
    def test_validate_question_id(self, create_question):
    
        # Arrange
        question_id = 1
        expected_output = True
        storage = SwapTestCaseStorageImplementation()
        storage.validate_question_id(question_id=question_id)
        
        # Act
        is_question_exists = Question.objects.filter(id=question_id).exists()
        
        # Assert
        assert expected_output == is_question_exists
    
    
    @pytest.mark.django_db
    def test_validate_invalid_question_id(self, create_question):
    
        # Arrange
        question_id = 2
        storage = SwapTestCaseStorageImplementation()
        
        # Assert
        with pytest.raises(InvalidQuestionId):
            storage.validate_question_id(question_id=question_id)
