import pytest
from content_management_portal.presenters.cleansolution_presenter_implementation \
    import PresenterImplementation
from content_management_portal.constants.exception_messages \
    import (
            INVALID_QUESTION_ID,
            INVALID_CLEANSOLUTION,
            INVALID_CLEAN_SOLUTION_FOR_QUESTION
            )
from django_swagger_utils.drf_server.exceptions import NotFound


class TestCleanSolutionPresenter:

    def test_get_response_for_list_of_cleansolution_dtos( \
                    self,list_of_cleansolution_dtos):
        # Arrange
    
        presenter = PresenterImplementation()
        actual_output = presenter.get_response_for_list_of_cleansolution_dtos( \
                    list_of_cleansolution_dtos=list_of_cleansolution_dtos)
        expected_output = [
                              {
                                "cleansolution_id": 1,
                                "code_type": "C",
                                "code": "str",
                                "filename": "str"
                              },
                              {
                                "cleansolution_id": 2,
                                "code_type": "PYTHON",
                                "code": "str",
                                "filename": "str"
                              },
    
                            ]
        # Act
        expected_output == actual_output


    def test_raise_exception_for_invalid_question(self):
    
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


    def test_raise_exception_for_invalid_prefilledcode(self):

        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_CLEANSOLUTION[0]
        exception_res_status = INVALID_CLEANSOLUTION[1]
    
        # Act
        with pytest.raises(NotFound) as exception:
            presenter.raise_invalid_cleansolution_exception()
    
        # Assert
        assert exception.value.message == exception_message
        assert exception.value.res_status == exception_res_status
    
    
    def test_raise_exception_for_invalid_prefilledcode_for_invalid_question(self):

        # Arrange
        presenter = PresenterImplementation()
        exception_message = INVALID_CLEAN_SOLUTION_FOR_QUESTION[0]
        exception_res_status = INVALID_CLEAN_SOLUTION_FOR_QUESTION[1]
    
        # Act
        with pytest.raises(NotFound) as exception:
            presenter.raise_invalid_cleansolution_for_question_exception()
    
        # Assert
        assert exception.value.message == exception_message
        assert exception.value.res_status == exception_res_status
