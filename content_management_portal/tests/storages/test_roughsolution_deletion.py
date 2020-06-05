import pytest

from content_management_portal.models import RoughSolution
from content_management_portal.storages.roughsolution_storage_implementation import \
    RoughStorageImplementation



@pytest.mark.django_db
def test_roughsolution_deletion(create_roughsolution):

    # Arrange
    question_id = 1
    rough_solution_id = 1
    expected_output = False
    storage = RoughStorageImplementation()
    storage.rough_solution_deletion( 
                                    question_id=question_id,
                                    rough_solution_id=rough_solution_id
                                    )   
    
    # Act
    is_roughsolution_exists = RoughSolution.objects.filter(
        question_id=question_id,id=rough_solution_id
    ).exists()
    
    # Assert
    assert expected_output == is_roughsolution_exists


    
    