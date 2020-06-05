import pytest
from content_management_portal.presenters. \
    getquestion_presenter_implementation import PresenterImplementation
from django_swagger_utils.drf_server.exceptions import NotFound

from content_management_portal.constants.exception_messages \
    import INVALID_QUESTION_ID


def test_get_question_dto_response(questiondto):
    # Arrange
    presenter = PresenterImplementation()
    question_dto = questiondto
    list_of_roughsolution_dtos = []
    list_of_testcase_dtos = []
    list_of_prefilledcode_dtos = []
    solutionapproach_dto = None
    list_of_cleansolution_dtos = []
    list_of_hint_dtos = []

    # Act
    actual_output = presenter.get_question_dto_response(
        question_dto,
        list_of_roughsolution_dtos,
        list_of_testcase_dtos,
        list_of_prefilledcode_dtos,
        solutionapproach_dto,
        list_of_cleansolution_dtos,
        list_of_hint_dtos
        )

    expected_output = {"question_details": {"question_id": 1, "short_title": "string", "problem_description": {"content_type": "HTML", "content": "string"}}, "roughsolutions": [], "testcases": [], "prefilledcodes": [], "solutionapproaches": [], "cleansolutions": [], "hints": []}

    # Act
    expected_output == actual_output


def test_raise_invalid_question_exception():
    
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
   