import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec, patch

from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
    login_user_presenter_interface import PresenterInterface
from content_management_portal.interactors.user_login_interactor \
    import UserLoginInteractor
from content_management_portal.interactors.storages.dtos import AccessTokenDto
from content_management_portal.exceptions import (
    InvalidUserName,
    InvalidPassword
    )


def test_login_with_username_and_password_returns_access_token():
    # Arrange
    username = "srinu"
    password = "12345"
    user_id = 1
    access_token = "1234"
    
    access_token_dto = AccessTokenDto(
                        access_token="1234",
                        refresh_token="123",
                        expires_in=100000000
                        )
    
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    
    storage.validate_username.return_value = user_id
    
    interactor = UserLoginInteractor(
                        storage=storage,
                        presenter=presenter,
                        oauth_storage=oauth_storage
                        )
    
    # Act
    with patch.object(OAuthUserAuthTokensService, \
                    'create_user_auth_tokens',return_value=access_token_dto):
                    interactor.login_user(username=username,
                                          password=password
                                        )
    
    # Assert
    storage.validate_username.assert_called_once_with(username=username)
    storage.validate_password.assert_called_once_with(
        username=username,password=password)
    presenter.get_response_for_access_token.assert_called_once_with( \
                access_token=access_token)
                
def test_login_with_invalid_username_raises_exception():
        # Arrange
        username = 'srinu'
        password = 'password'
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        oauth_storage = create_autospec(OAuth2SQLStorage)
    
        interactor = UserLoginInteractor(
                        storage=storage,
                        presenter=presenter,
                        oauth_storage=oauth_storage
                        )
    
    
        storage.validate_username.side_effect = InvalidUserName
        presenter.raise_invalid_user_name_exception.side_effect = NotFound
    
        # Act
        with pytest.raises(NotFound):
            interactor.login_user(username=username, password=password)
    
        # Assert
        storage.validate_username.assert_called_once_with(
            username=username
        )
        presenter.raise_invalid_user_name_exception. \
            assert_called_once()
    
