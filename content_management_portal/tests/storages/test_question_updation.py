import pytest

from content_management_portal.models import Question
from content_management_portal.storages.question_storage_implementation import \
    QuestionStorageImplementation
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )

@pytest.mark.django_db
def test_question_updation(create_user, create_question, question_dtos):

    question = create_question
    user_id=1
    question_id = 1
    short_title = "even"
    content_type = TextType.html.value
    content = "helloworld"
    storage = QuestionStorageImplementation()

    question_dtos = storage.question_updation(
                user_id=user_id,
                short_title=short_title,
                content_type=content_type,
                content=content,
                question_id=question_id
                )

    # Act

    assert question_dtos.short_title==short_title
    assert question_dtos.content_type==content_type
    assert question_dtos.content==content
    assert question_dtos.question_id==question_id
