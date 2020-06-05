import pytest
from django_swagger_utils.drf_server.exceptions import NotFound

from content_management_portal.constants.exception_messages import \
    (
        INVALID_TESTCASE_ID,
        INVALID_TESTCASE_FOR_QUESTION
    )
from content_management_portal.presenters.testcase_presenter_implementation \
    import PresenterImplementation

class TestTestcase:

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
        
    def test_get_response_for_testcase(self,testcase_dto):
        
        # Arrange
        presenter = PresenterImplementation()
        expected_result = {
            "order_id": 1,
            "testcase_id": 1,
            "input": "string",
            "output": "string",
            "is_hidden": True,
            "score": 1,
            "question_id": 1
        }
        
        # Act
        actual_result = presenter.get_response_for_testcase( \
                                        testcase_dto=testcase_dto)
        
        # Assert
        assert actual_result == expected_result
        
