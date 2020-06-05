import pytest

from content_management_portal.models import Question
from content_management_portal.storages. \
    login_user_storage_implementation import UserStorageImplementation
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )
from content_management_portal.exceptions import (
    InvalidUserName,
    InvalidPassword
    )


@pytest.mark.django_db
def test_valid_username(create_user):

    # Arrange
    username = "srinu"
    expected_output = 1
    
    storage = UserStorageImplementation()
    
    # Act
    actual_output = storage.validate_username(username=username)

    # Assert
    expected_output == actual_output
    
@pytest.mark.django_db
def test_invalid_username():

    # Arrange
    username = "haha"
    
    storage = UserStorageImplementation()
    
    # Assert
    with pytest.raises(InvalidUserName):
        storage.validate_username(username=username)

    