import pytest

from content_management_portal.exceptions.exceptions import InvalidQuestionId
from content_management_portal.models import Question
from content_management_portal.storages.roughsolution_storage_implementation import \
    RoughStorageImplementation


@pytest.mark.django_db
def test_validate_question_id(create_question):

    # Arrange
    question_id = 1
    expected_output = True
    storage = RoughStorageImplementation()
    storage.validate_question_id(question_id=question_id)
    
    # Act
    is_question_exists = Question.objects.filter(id=question_id).exists()
    
    # Assert
    assert expected_output == is_question_exists


@pytest.mark.django_db
def test_validate_invalid_question_id(create_question):

    # Arrange
    question_id = 2
    storage = RoughStorageImplementation()
    
    # Assert
    with pytest.raises(InvalidQuestionId):
        storage.validate_question_id(question_id=question_id)

    
    