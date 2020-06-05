import pytest

from content_management_portal.models import Question
from content_management_portal.storages.login_user_storage_implementation import \
    UserStorageImplementation
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )
from content_management_portal.exceptions import (
    InvalidUserName,
    InvalidPassword
    )
from content_management_portal.models.user import User

@pytest.mark.django_db
def test_invalid_password(create_user):

    # Arrange
    username = "srinu"
    password="123"
    
    storage = UserStorageImplementation()
    
    # Assert
    with pytest.raises(InvalidPassword):
        storage.validate_password(username=username,password=password)

    