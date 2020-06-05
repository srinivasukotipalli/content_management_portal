import pytest

from content_management_portal.models import \
    (
        RoughSolution,
        Question,
        Case,
        SolutionApproach,
        CleanSolution,
        Hint,
        PrefilledCode
    )
from content_management_portal.storages.get_question_storage_implementation \
    import GetQuestionStorageImplementation
from content_management_portal.exceptions.exceptions import InvalidQuestionId

@pytest.mark.django_db
def test_get_questions(
                question_id_dtos,
                create_roughsolution,
                rough_solution_id_dto,
                create_prefilledcode,
                prefilledcodeiddto,
                create_cleansolution,
                cleansolutioniddto,
                create_hint,
                hint_dto,
                create_testcase,
                testcase_dto
                ):
                

    # Arrange

    storage = GetQuestionStorageImplementation()
    question_id = 1
    
    
    question_dto,list_of_roughsolution_dtos, list_of_testcase_dtos, list_of_prefilledcode_dtos, solutionapproach_dto, list_of_cleansolution_dtos, list_of_hint_dtos = storage.get_question(question_id=question_id)

    # Act
    
    assert question_dto == question_dto
    assert list_of_roughsolution_dtos == [rough_solution_id_dto]
    assert list_of_prefilledcode_dtos == [prefilledcodeiddto]
    assert list_of_cleansolution_dtos == [cleansolutioniddto]
    assert list_of_hint_dtos == [hint_dto]
    assert list_of_testcase_dtos == [testcase_dto]


@pytest.mark.django_db
def test_get_question(question_id_dtos):
                
    # Arrange
    
    storage = GetQuestionStorageImplementation()
    question_id = 1
    question_dto = question_id_dtos

    # Act
    question_dto,list_of_roughsolution_dtos, list_of_testcase_dtos, list_of_prefilledcode_dtos, solutionapproach_dto, list_of_cleansolution_dtos, list_of_hint_dtos = storage.get_question(question_id=question_id)

    
    # Assert
    assert question_dto == question_dto
    assert list_of_roughsolution_dtos == []
    assert list_of_prefilledcode_dtos == []
    assert list_of_cleansolution_dtos == []
    assert list_of_hint_dtos == []
    assert list_of_testcase_dtos == []
    assert solutionapproach_dto == None

    

@pytest.mark.django_db
def test_validate_invalid_question_id():
    
    # Arrange
    storage = GetQuestionStorageImplementation()
    question_id = 2
    
    # Assert
    
    with pytest.raises(InvalidQuestionId):
        storage.validate_question_id(question_id=question_id)

    
@pytest.mark.django_db
def test_validate_valid_question_id(create_question):
    
    # Arrange
    storage = GetQuestionStorageImplementation()
    question_id = 1
    
    # Assert
    result = storage.validate_question_id(question_id=question_id)

    # Act
    assert result == None
