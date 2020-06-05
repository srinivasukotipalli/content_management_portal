import pytest
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

from content_management_portal.constants.exception_messages import \
    INVALID_OFFSET_VALUE
from content_management_portal.presenters. \
    coding_questions_presenter_implementation import PresenterImplementation


def test_raise_exception_for_invalid_offset():

    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_OFFSET_VALUE[0]
    exception_res_status = INVALID_OFFSET_VALUE[1]

    # Act
    with pytest.raises(BadRequest) as exception:
        presenter.raise_is_invalid_offset_value()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
