import pytest

from content_management_portal.exceptions.exceptions import InvalidRoughSolutionId
from content_management_portal.models import RoughSolution
from content_management_portal.storages.roughsolution_storage_implementation import \
    RoughStorageImplementation


@pytest.mark.django_db
def test_validate_roughsolution_id(create_roughsolution_list):

    # Arrange
    list_of_rough_solutions_ids = [1,2]
    expected_output = True
    storage = RoughStorageImplementation()
    storage.validate_rough_solution_ids( \
                list_of_rough_solutions_ids=list_of_rough_solutions_ids)

    # Act
    output = [1,2] == [1,2]
    
    # Assert
    assert expected_output == output


@pytest.mark.django_db
def test_validate_invalid_roughsolution_id(create_roughsolution_list):

    # Arrange
    list_of_rough_solutions_ids = [2,3]
    expected_output = False
    storage = RoughStorageImplementation()
    
    # Assert
    with pytest.raises(InvalidRoughSolutionId):
        storage.validate_rough_solution_ids( \
                list_of_rough_solutions_ids=list_of_rough_solutions_ids)
    

    
    