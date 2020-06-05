import pytest
from content_management_portal.presenters. \
  coding_questions_presenter_implementation import PresenterImplementation


def test_get_response_for_all_coding_questions(total_questions_dtos_list):
    
    total_coding_questions = 1
    expected_output = {
                          "total_coding_questions": 1,
                          "question_details": [
                            {
                              "question_id": 1,
                              "short_title": "even",
                              "roughsolution": True,
                              "testcase": False,
                              "prefilledcode": False,
                              "solutionapproach": False,
                              "cleansolution": False,
                              "hint": False
                            }
                          ]
                        } 
                        
    presenter = PresenterImplementation()
    actual_output = presenter.get_response_for_all_the_questions( \
                        total_questions_dtos_list=total_questions_dtos_list, \
                            total_coding_questions=total_coding_questions)
    
    # Act
    assert actual_output == expected_output