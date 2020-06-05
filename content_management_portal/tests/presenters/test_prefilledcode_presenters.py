import pytest
from content_management_portal.presenters.prefilledcode_presenter_implementation \
	import PresenterImplementation
from content_management_portal.constants.exception_messages \
	import (
			INVALID_QUESTION_ID,
			INVALID_PREFILLED_CODE,
			INVALID_PREFILLED_CODE_FOR_QUESTION
			)
from django_swagger_utils.drf_server.exceptions import NotFound


class TestPrefilledcodePresenter:

	def test_get_response_for_list_of_prefilledcode_dtos(self,list_of_prefilledcode_dtos):
		# Arrange
	
		presenter = PresenterImplementation()
		actual_output = presenter.get_response_for_list_of_prefilledcode_dtos( \
					list_of_prefilledcode_dtos=list_of_prefilledcode_dtos)
		expected_output = [
							  {
							    "prefilledcode_id": 1,
							    "code_type": "C",
							    "code": "str",
							    "filename": "str"
							  },
							  {
							    "prefilledcode_id": 2,
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
	    exception_message = INVALID_PREFILLED_CODE[0]
	    exception_res_status = INVALID_PREFILLED_CODE[1]
	
	    # Act
	    with pytest.raises(NotFound) as exception:
	        presenter.raise_invalid_prefilledcode_exception()
	
	    # Assert
	    assert exception.value.message == exception_message
	    assert exception.value.res_status == exception_res_status
	
	
	def test_raise_exception_for_invalid_prefilledcode_for_invalid_question(self):

	    # Arrange
	    presenter = PresenterImplementation()
	    exception_message = INVALID_PREFILLED_CODE_FOR_QUESTION[0]
	    exception_res_status = INVALID_PREFILLED_CODE_FOR_QUESTION[1]
	
	    # Act
	    with pytest.raises(NotFound) as exception:
	        presenter.raise_invalid_prefilledcode_for_question_exception()
	
	    # Assert
	    assert exception.value.message == exception_message
	    assert exception.value.res_status == exception_res_status
