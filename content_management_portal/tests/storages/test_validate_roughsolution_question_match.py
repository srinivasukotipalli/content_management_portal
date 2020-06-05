import pytest

from content_management_portal.exceptions.exceptions import \
    InvalidRoughSolutionForQuestion
from content_management_portal.models import Question
from content_management_portal.storages.roughsolution_storage_implementation import \
    RoughStorageImplementation


@pytest.mark.django_db
def test_validate_roughsolution_invalid_question_match(create_roughsolution_list):

    # Arrange
    question_id = 1
    list_of_rough_solutions_ids = [3,4]
    storage = RoughStorageImplementation()
    
    # Assert
    with pytest.raises(InvalidRoughSolutionForQuestion):
        storage.validate_question_roughsolutions_match( \
        question_id=question_id,
        list_of_rough_solutions_ids=list_of_rough_solutions_ids)
    
        
@pytest.mark.django_db
def test_validate_roughsolution_valid_question_match(create_roughsolution_list):

    # Arrange
    question_id = 1
    list_of_rough_solutions_ids = [1,2]
    storage = RoughStorageImplementation()
    expected_output = [1,2]
    # Act
    storage.validate_question_roughsolutions_match( \
        question_id=question_id,
        list_of_rough_solutions_ids=list_of_rough_solutions_ids)
    # output=[1,2]
    # # Assert
    # assert expected_output==output
