import pytest
from django_swagger_utils.drf_server.exceptions import NotFound

from content_management_portal.constants.exception_messages import \
    (
        INVALID_TESTCASE_ID,
        INVALID_TESTCASE_FOR_QUESTION,
        INVALID_QUESTION_ID
    )
from content_management_portal.presenters.swap_testcase_presenter_implementation \
    import PresenterImplementation

class TestSwapTestcase:

    def test_raise_exception_for_invalid_testcase(self):
    
        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_TESTCASE_ID[0]
        exception_res_status = INVALID_TESTCASE_ID[1]
    
        # Act
        with pytest.raises(NotFound) as exception:
            presenter.raise_invalid_testcase_exception()
    
        # Assert
        assert exception.value.message == exception_message
        assert exception.value.res_status == exception_res_status
    
    def test_raise_invalid_testcase_for_question_exception(self):
    
        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_TESTCASE_FOR_QUESTION[0]
        exception_res_status = INVALID_TESTCASE_FOR_QUESTION[1]
    
        # Act
        with pytest.raises(NotFound) as exception:
            presenter.raise_invalid_testcase_for_question_exception()
    
        # Assert
        assert exception.value.message == exception_message
        assert exception.value.res_status == exception_res_status
    
    
    def test_raise_invalid_question_exception(self):
    
        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_QUESTION_ID[0]
        exception_res_status = INVALID_QUESTION_ID[1]
    
        # Act
        with pytest.raises(NotFound) as exception:
            presenter.raise_invalid_question_exception()
    
        # Assert
        assert exception.value.message == exception_message
        assert exception.value.res_status == exception_res_status
    
    