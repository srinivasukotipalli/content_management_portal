import pytest
from django_swagger_utils.drf_server.exceptions import NotFound

from content_management_portal.constants.exception_messages import INVALID_PASSWORD
from content_management_portal.presenters. \
    login_user_presenter_implementation import PresenterImplementation


def test_raise_exception_for_invalid_question():

    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_PASSWORD[0]
    exception_res_status = INVALID_PASSWORD[1]

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_password_exception()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
