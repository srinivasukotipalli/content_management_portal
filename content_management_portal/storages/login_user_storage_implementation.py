from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )

 
from content_management_portal.models import User
from content_management_portal.exceptions import (
    InvalidUserName,
    InvalidPassword
    )


class UserStorageImplementation(StorageInterface):


    def validate_username(self, username: str)->int:
        try:
            user = User.objects.get(username=username)
            return user.id
            
        except User.DoesNotExist:
            raise InvalidUserName 

    def validate_password(self,username=str, password=str):
        user = User.objects.get(username=username)
        if not user.check_password(password):
            raise InvalidPassword
