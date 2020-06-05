import pytest

from content_management_portal.models import Question, CleanSolution
from content_management_portal.storages.cleansolution_storage_implementation import \
    CleanSolutionStorageImplementation
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )
from content_management_portal.exceptions.exceptions import \
    (
        InvalidQuestionId,
        InvalidCleanSolutionId,
        InvalidCleanSolutionForQuestion
    )


class TestCleanSolution:

    @pytest.mark.django_db
    def test_cleansolution_creation_and_updation(self, create_user, \
                        create_question, cleansolutiondto, cleansolutioniddto):

        question_id = 1
        code_type = "PYTHON"
        code = "str"
        filename = "str"

        storage = CleanSolutionStorageImplementation()
        list_of_question_cleansolution_dtos = \
                storage.updation_and_creation_of_cleansolutions( \
                                question_id=question_id,
                                updated_cleansolution_dtos=[cleansolutioniddto],
                                created_cleansolution_dtos=[cleansolutiondto]
                                )


        # Act
        for question_dtos in list_of_question_cleansolution_dtos:
            assert question_dtos.code_type==code_type
            assert question_dtos.code==code
            assert question_dtos.filename==filename
            assert question_dtos.question_id==question_id


    @pytest.mark.django_db
    def test_cleansolution_deletion(self,create_cleansolution):

        # Arrange
        question_id = 1
        cleansolution_id = 1
        expected_output = False
        storage = CleanSolutionStorageImplementation()
        storage.cleansolution_deletion(
                                        question_id=question_id,
                                        cleansolution_id=cleansolution_id
                                        )

        # Act
        is_cleansolution_exists = CleanSolution.objects.filter(
            question_id=question_id,id=cleansolution_id
        ).exists()

        # Assert
        assert expected_output == is_cleansolution_exists


    @pytest.mark.django_db
    def test_validate_question_id(self, create_question):

        # Arrange
        question_id = 1
        expected_output = True
        storage = CleanSolutionStorageImplementation()
        storage.validate_question_id(question_id=question_id)

        # Act
        is_question_exists = Question.objects.filter(id=question_id).exists()

        # Assert
        assert expected_output == is_question_exists


    @pytest.mark.django_db
    def test_validate_invalid_question_id(self, create_question):

        # Arrange
        question_id = 2
        storage = CleanSolutionStorageImplementation()

        # Assert
        with pytest.raises(InvalidQuestionId):
            storage.validate_question_id(question_id=question_id)

    @pytest.mark.django_db
    def test_validate_cleansolution_id(self,create_cleansolution_list):

        # Arrange
        list_of_cleansolution_ids = [1,2]
        expected_output = True
        storage = CleanSolutionStorageImplementation()
        storage.validate_cleansolution_ids( \
                    list_of_cleansolution_ids=list_of_cleansolution_ids)

        # Act
        output = [1,2] == [1,2]

        # Assert
        assert expected_output == output


    @pytest.mark.django_db
    def test_validate_invalid_cleansolution_id(self, create_cleansolution_list):

        # Arrange
        list_of_cleansolution_ids = [2,3]
        storage = CleanSolutionStorageImplementation()

        # Assert
        with pytest.raises(InvalidCleanSolutionId):
            storage.validate_cleansolution_ids( \
                    list_of_cleansolution_ids=list_of_cleansolution_ids)

    @pytest.mark.django_db
    def test_validate_cleansolution_invalid_question_match( \
                self, create_cleansolution_list):

        # Arrange
        question_id = 1
        list_of_cleansolution_ids = [3,4]
        storage = CleanSolutionStorageImplementation()
        
        # Assert
        with pytest.raises(InvalidCleanSolutionForQuestion):
            storage.validate_question_cleansolution_match( \
                        question_id=question_id,
                        list_of_cleansolution_ids=list_of_cleansolution_ids)
                    
        
    @pytest.mark.django_db
    def test_validate_cleansolution_valid_question_match( \
                self, create_cleansolution_list):
    
        # Arrange
        question_id = 1
        list_of_cleansolution_ids = [1,2]
        storage = CleanSolutionStorageImplementation()
    
        # Act
        storage.validate_question_cleansolution_match( \
            question_id=question_id,
            list_of_cleansolution_ids=list_of_cleansolution_ids)
