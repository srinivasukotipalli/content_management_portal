import pytest
from django_swagger_utils.drf_server.exceptions import NotFound

from content_management_portal.constants.enums import TextType
from content_management_portal.constants.exception_messages import \
    (
        INVALID_SOLUTIONAPPROACH_ID,
        INVALID_SOLUTIONAPPROACH_FOR_QUESTION
    )
from content_management_portal.presenters.solutionapproach_presenter_implementation \
    import PresenterImplementation

class TestSolutionApproach:

    def test_raise_exception_for_invalid_solutionapproach(self):
    
        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_SOLUTIONAPPROACH_ID[0]
        exception_res_status = INVALID_SOLUTIONAPPROACH_ID[1]
    
        # Act
        with pytest.raises(NotFound) as exception:
            presenter.raise_invalid_solutionapproach_exception()
    
        # Assert
        assert exception.value.message == exception_message
        assert exception.value.res_status == exception_res_status
    
    def raise_invalid_solutionapproach_for_question_exception(self):
    
        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_SOLUTIONAPPROACH_FOR_QUESTION[0]
        exception_res_status = INVALID_SOLUTIONAPPROACH_FOR_QUESTION[1]
    
        # Act
        with pytest.raises(NotFound) as exception:
            presenter.raise_invalid_solutionapproach_exception()
    
        # Assert
        assert exception.value.message == exception_message
        assert exception.value.res_status == exception_res_status
        
    def test_get_response_for_solutionapproach(self,solutionapproach_dto):
        
        # Arrange
        presenter = PresenterImplementation()
        expected_result = {
            "solutionapproach_id": 1,
            "title": "string",
            "description_content_type": TextType.html.value,
            "description_content": "string",
            "complexity_analysis_content_type": TextType.html.value,
            "complexity_analysis_content": "string",
        }
        
        # Act
        actual_result = presenter.get_response_for_solutionapproach( \
                                    solutionapproach_dto=solutionapproach_dto)
        
        # Assert
        assert actual_result == expected_result
        
