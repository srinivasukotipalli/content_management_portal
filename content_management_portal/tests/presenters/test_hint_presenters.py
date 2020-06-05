import pytest
from django_swagger_utils.drf_server.exceptions import NotFound

from content_management_portal.constants.enums import TextType
from content_management_portal.constants.exception_messages import \
    (
        INVALID_HINT_ID,
        INVALID_HINT_FOR_QUESTION
    )
from content_management_portal.presenters.hint_presenter_implementation \
    import PresenterImplementation

class TestHint:

    def test_raise_exception_for_invalid_hint(self):
    
        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_HINT_ID[0]
        exception_res_status = INVALID_HINT_ID[1]
    
        # Act
        with pytest.raises(NotFound) as exception:
            presenter.raise_invalid_hint_exception()
    
        # Assert
        assert exception.value.message == exception_message
        assert exception.value.res_status == exception_res_status
    
    def raise_invalid_hint_for_question_exception(self):
    
        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_HINT_FOR_QUESTION[0]
        exception_res_status = INVALID_HINT_FOR_QUESTION[1]
    
        # Act
        with pytest.raises(NotFound) as exception:
            presenter.raise_invalid_hint_for_question_exception()
    
        # Assert
        assert exception.value.message == exception_message
        assert exception.value.res_status == exception_res_status
        
    def test_get_response_for_hint(self,hint_dto):
        
        # Arrange
        presenter = PresenterImplementation()
        expected_result = {
            "hint_id": 1,
            "title": "string",
            "content_type": TextType.html.value,
            "content": "string",
            "order_id": 1,
            "question_id": 1
        }
        
        # Act
        actual_result = presenter.get_response_for_hint(hint_dto=hint_dto)
        
        # Assert
        assert actual_result == expected_result
        
