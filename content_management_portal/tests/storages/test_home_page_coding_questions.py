import pytest

from content_management_portal.models import Question
from content_management_portal.storages.home_page_coding_questions_implementation \
    import HomeStorageImplementation

@pytest.mark.django_db
def test_home_page_coding_questions(
        total_questions_dtos_list,create_question,create_roughsolution):

    # Arrange
    offset = 0
    limit = 2
    
    storage = HomeStorageImplementation()
    expected_coding_questions_output = 1
    
    
    actual_total_questions_dtos_list,actual_total_coding_questions = \
                    storage.get_question_details(offset=offset,limit=limit)

    # Act
    
    assert actual_total_questions_dtos_list==total_questions_dtos_list
    assert actual_total_coding_questions==expected_coding_questions_output
