import pytest
from content_management_portal.presenters.login_user_presenter_implementation \
    import PresenterImplementation


def test_raise_exception_for_invalid_accesstoken():

    # Arrange
    presenter = PresenterImplementation()
    access_token="123"
    expected_output = {"access_token": "123"}
    
    # Act
    actual_output = presenter.get_response_for_access_token( \
                        access_token=access_token)

    # Assert
    expected_output == actual_output
    