import pytest

from content_management_portal.models import Question, Hint
from content_management_portal.storages.hint_storage_implementation import \
    HintStorageImplementation


class TestHint:

    @pytest.mark.django_db
    def test_hint_creation(self, hint_dto):
    
        # Arrange
        question_id = 1
        storage = HintStorageImplementation()
        actual_hint_dto = storage.hint_creation( \
                                            question_id=question_id,
                                            created_hint_dto=hint_dto
                                        )
    
        # Act
        assert actual_hint_dto.hint_id ==hint_dto.hint_id
        assert actual_hint_dto.title==hint_dto.title
        assert actual_hint_dto.content==hint_dto.content
        assert actual_hint_dto.content_type==hint_dto.content_type
        assert actual_hint_dto.order_id==hint_dto.order_id
        assert actual_hint_dto.question_id==hint_dto.question_id

    @pytest.mark.django_db
    def test_hint_updation(self, create_hint, hint_dto):
    
        # Arrange
        question_id = 1
        storage = HintStorageImplementation()
        actual_hint_dto = storage.hint_updation( \
                                            question_id=question_id,
                                            updated_hint_dto=hint_dto
                                        )
    
        # Act
        assert actual_hint_dto.hint_id ==hint_dto.hint_id
        assert actual_hint_dto.title==hint_dto.title
        assert actual_hint_dto.content==hint_dto.content
        assert actual_hint_dto.content_type==hint_dto.content_type
        assert actual_hint_dto.order_id==hint_dto.order_id
        assert actual_hint_dto.question_id==hint_dto.question_id
        
    @pytest.mark.django_db
    def test_hint_deletion(self, create_hint):

        # Arrange
        question_id = 1
        hint_id = 1
        storage = HintStorageImplementation()
        expected_result = False
        
        # Act
        storage.hint_deletion(
                        question_id=question_id,
                        hint_id=hint_id
                        )
                        
        actual_result = Hint.objects.filter( \
                                question_id=hint_id,id=hint_id).exists()
        
        # Arrange
        assert expected_result == actual_result
        
    @pytest.mark.django_db
    def test_validate_question_hint_match(self, create_hint):
        # Arrange
        question_id = 1
        hint_id = 1
        storage = HintStorageImplementation()
        expected_result = True
        
        # Act
        actual_result = storage.validate_question_hint_match(
                        question_id=question_id,
                        hint_id=hint_id
                        )
                        
        # Arrange
        assert expected_result == actual_result
    
    @pytest.mark.django_db
    def test_validate_hint_id(self, create_hint):
        
        # Arrange
        hint_id = 1
        storage = HintStorageImplementation()
        expected_result = True
        
        # Act
        actual_result = storage.validate_hint_id(hint_id=hint_id)
                        
        # Arrange
        assert expected_result == actual_result
    
    @pytest.mark.django_db
    def test_validate_question_id(self, create_question):
        
        # Arrange
        question_id = 1
        storage = HintStorageImplementation()
        expected_result = None
        
        # Act
        actual_result = storage.validate_question_id(question_id=question_id)
                        
        # Arrange
        assert expected_result == actual_result
    
    