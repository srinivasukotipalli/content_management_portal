import pytest

from content_management_portal.models import Question
from content_management_portal.storages.roughsolution_storage_implementation import \
    RoughStorageImplementation
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )

@pytest.mark.django_db
def test_roughsolution_creation_and_updation( \
            create_user, create_question, rough_solution_dto, rough_solution_id_dto):

    question = create_question
    question_id = 1
    code_type = "PYTHON"
    code = "str"
    filename = "str"

    storage = RoughStorageImplementation()
    list_of_question_dtos = storage.updation_and_creation_of_rough_solutions( \
                question_id=question_id,
                updated_rough_solutions_dtos=[rough_solution_id_dto],
                created_rough_solutions_dtos=[rough_solution_dto]
                )
    
    
    # Act
    for question_dtos in list_of_question_dtos:
        assert question_dtos.code_type==code_type
        assert question_dtos.code==code
        assert question_dtos.filename==filename
        assert question_dtos.question_id==question_id

        