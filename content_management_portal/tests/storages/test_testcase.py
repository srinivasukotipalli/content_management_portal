import pytest

from content_management_portal.models import Question, Case
from content_management_portal.storages.testcase_storage_implementation import \
    CaseStorageImplementation


class TestTestcase:

    @pytest.mark.django_db
    def test_testcase_creation(self, testcase_dto):
    
        # Arrange
        question_id = 1
        storage = CaseStorageImplementation()
        actual_testcase_dto = storage.testcase_creation( \
                                            question_id=question_id,
                                            created_testcase_dto=testcase_dto
                                        )
    
        # Act
        assert actual_testcase_dto.order_id ==testcase_dto.order_id
        assert actual_testcase_dto.testcase_id ==testcase_dto.testcase_id
        assert actual_testcase_dto.input==testcase_dto.input
        assert actual_testcase_dto.output==testcase_dto.output
        assert actual_testcase_dto.is_hidden==testcase_dto.is_hidden
        assert actual_testcase_dto.score==testcase_dto.score
        assert actual_testcase_dto.question_id==testcase_dto.question_id

    @pytest.mark.django_db
    def test_testcase_updation(self, create_testcase, testcase_dto):
    
        # Arrange
        question_id = 1
        storage = CaseStorageImplementation()
        actual_testcase_dto = storage.testcase_updation( \
                                            question_id=question_id,
                                            updated_testcase_dto=testcase_dto
                                        )
    
        # Act
        assert actual_testcase_dto.order_id ==testcase_dto.order_id
        assert actual_testcase_dto.testcase_id ==testcase_dto.testcase_id
        assert actual_testcase_dto.input==testcase_dto.input
        assert actual_testcase_dto.output==testcase_dto.output
        assert actual_testcase_dto.is_hidden==testcase_dto.is_hidden
        assert actual_testcase_dto.score==testcase_dto.score
        assert actual_testcase_dto.question_id==testcase_dto.question_id

    @pytest.mark.django_db
    def test_testcase_deletion(self, create_testcase):
        # Arrange
        question_id = 1
        testcase_id = 1
        storage = CaseStorageImplementation()
        expected_result = False
        
        # Act
        storage.testcase_deletion(
                        question_id=question_id,
                        testcase_id=testcase_id
                        )
                        
        actual_result = Case.objects.filter( \
                                question_id=question_id,id=testcase_id).exists()
        
        # Arrange
        assert expected_result == actual_result
        
    @pytest.mark.django_db
    def test_validate_question_testcase_match(self, create_testcase):
        # Arrange
        question_id = 1
        testcase_id = 1
        storage = CaseStorageImplementation()
        expected_result = True
        
        # Act
        actual_result = storage.validate_question_testcase_match(
                        question_id=question_id,
                        testcase_id=testcase_id
                        )
                        
        # Arrange
        assert expected_result == actual_result
    
    @pytest.mark.django_db
    def test_validate_testcase_id(self, create_testcase):
        
        # Arrange
        testcase_id = 1
        storage = CaseStorageImplementation()
        expected_result = True
        
        # Act
        actual_result = storage.validate_testcase_id(testcase_id=testcase_id)
                        
        # Arrange
        assert expected_result == actual_result
    
    @pytest.mark.django_db
    def test_validate_question_id(self, create_question):
        
        # Arrange
        question_id = 1
        storage = CaseStorageImplementation()
        expected_result = None
        
        # Act
        actual_result = storage.validate_question_id(question_id=question_id)
                        
        # Arrange
        assert expected_result == actual_result
    
    