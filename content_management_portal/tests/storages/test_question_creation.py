import pytest

from content_management_portal.models import Question
from content_management_portal.storages.question_storage_implementation import \
    QuestionStorageImplementation
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )


@pytest.mark.django_db
def test_question_creation(
    create_user, question_dtos):

    # Arrange
    user_id = 1
    #question = create_question
    short_title = "even"
    content_type = TextType.html.value
    content = "helloworld"
    storage = QuestionStorageImplementation()

    questiondtos = storage.question_creation(
                user_id = user_id,
                short_title=short_title,
                content_type=content_type,
                content=content
                )

    # Act
    
    assert questiondtos.short_title==short_title
    assert questiondtos.content_type==content_type
    assert questiondtos.content==content
    assert questiondtos.user_id==user_id
    