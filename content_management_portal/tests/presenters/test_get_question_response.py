from content_management_portal.presenters. \
	question_presenter_implementation import PresenterImplementation
	
	
def test_get_question_dto_response(questiondto):
	# Arrange
	presenter = PresenterImplementation()
	actual_output = presenter.get_question_dto_response(questiondto=questiondto)
	expected_output = {
						  "question_id": 0,
						  "short_title": "string",
						  "problem_description": {
						    "content_type": "MARKDOWN",
						    "content": "string"
						  }
						}
	# Act
	expected_output == actual_output
				