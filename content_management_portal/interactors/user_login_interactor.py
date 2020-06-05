from content_management_portal.interactors.storages.storage_interface import StorageInterface
from common.oauth2_storage import OAuth2SQLStorage
from content_management_portal.interactors.presenters. \
                login_user_presenter_interface import PresenterInterface
from common.oauth_user_auth_tokens_service import  OAuthUserAuthTokensService
from content_management_portal.exceptions import (
    InvalidUserName,
    InvalidPassword
    )

class UserLoginInteractor:
    def __init__(self, storage: StorageInterface,
                 oauth_storage: OAuth2SQLStorage,
                 presenter: PresenterInterface):
        self.storage = storage
        self.oauth_storage = oauth_storage
        self.presenter = presenter

    def login_user(self, username: str, password: str):

        # validate_user

        try:
            user_id = self.storage.validate_username(username=username)
        except InvalidUserName:
            self.presenter.raise_invalid_user_name_exception()
            return

        # validate_password
        try:
            self.storage.validate_password(username=username, password=password)
        except InvalidPassword:
            self.presenter.raise_invalid_password_exception()
            return

        service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth_storage
        )

        dto = service.create_user_auth_tokens(user_id=user_id)
        response = self.presenter.get_response_for_access_token(access_token=dto.access_token)
        return response