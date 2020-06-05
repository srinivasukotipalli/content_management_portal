import pytest

from content_management_portal.models import Question, PrefilledCode
from content_management_portal.storages.prefilledcode_storage_implementation import \
    PrefilledCodeStorageImplementation
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )
from content_management_portal.exceptions.exceptions import \
    (
        InvalidQuestionId,
        InvalidPrefilledCodeId,
        InvalidPrefilledCodeForQuestion
    )


class TestPrefilledCode:

    @pytest.mark.django_db
    def test_prefilledcode_creation_and_updation(self, create_user, \
                        create_question, prefilledcodedto, prefilledcodeiddto):

        question_id = 1
        code_type = "PYTHON"
        code = "str"
        filename = "str"

        storage = PrefilledCodeStorageImplementation()
        list_of_question_prefilled_dtos = storage.updation_and_creation_of_prefilledcodes( \
                    question_id=question_id,
                    updated_prefilledcode_dtos=[prefilledcodeiddto],
                    created_prefilledcode_dtos=[prefilledcodedto]
                    )


        # Act
        for question_dtos in list_of_question_prefilled_dtos:
            assert question_dtos.code_type==code_type
            assert question_dtos.code==code
            assert question_dtos.filename==filename
            assert question_dtos.question_id==question_id


    @pytest.mark.django_db
    def test_prefilledcode_deletion(self,create_prefilledcode):

        # Arrange
        question_id = 1
        prefilledcode_id = 1
        expected_output = False
        storage = PrefilledCodeStorageImplementation()
        storage.prefilledcode_deletion(
                                        question_id=question_id,
                                        prefilledcode_id=prefilledcode_id
                                        )

        # Act
        is_prefilledcode_exists = PrefilledCode.objects.filter(
            question_id=question_id,id=prefilledcode_id
        ).exists()

        # Assert
        assert expected_output == is_prefilledcode_exists


    @pytest.mark.django_db
    def test_validate_question_id(self, create_question):

        # Arrange
        question_id = 1
        expected_output = True
        storage = PrefilledCodeStorageImplementation()
        storage.validate_question_id(question_id=question_id)

        # Act
        is_question_exists = Question.objects.filter(id=question_id).exists()

        # Assert
        assert expected_output == is_question_exists


    @pytest.mark.django_db
    def test_validate_invalid_question_id(self, create_question):

        # Arrange
        question_id = 2
        storage = PrefilledCodeStorageImplementation()

        # Assert
        with pytest.raises(InvalidQuestionId):
            storage.validate_question_id(question_id=question_id)

    @pytest.mark.django_db
    def test_validate_prefilledcode_id(self,create_prefilledcode_list):

        # Arrange
        list_of_prefilledcode_ids = [1,2]
        expected_output = True
        storage = PrefilledCodeStorageImplementation()
        storage.validate_prefilledcode_ids( \
                    list_of_prefilledcode_ids=list_of_prefilledcode_ids)

        # Act
        output = [1,2] == [1,2]

        # Assert
        assert expected_output == output


    @pytest.mark.django_db
    def test_validate_invalid_prefilledcode_id(self, create_prefilledcode_list):

        # Arrange
        list_of_prefilledcode_ids = [2,3]
        storage = PrefilledCodeStorageImplementation()

        # Assert
        with pytest.raises(InvalidPrefilledCodeId):
            storage.validate_prefilledcode_ids( \
                    list_of_prefilledcode_ids=list_of_prefilledcode_ids)

    @pytest.mark.django_db
    def test_validate_prefilledcode_invalid_question_match(self, create_prefilledcode_list):

        # Arrange
        question_id = 1
        list_of_prefilledcode_ids = [3,4]
        storage = PrefilledCodeStorageImplementation()
        
        # Assert
        with pytest.raises(InvalidPrefilledCodeForQuestion):
            storage.validate_question_prefilledcode_match( \
                        question_id=question_id,
                        list_of_prefilledcode_ids=list_of_prefilledcode_ids)
                    
        
    @pytest.mark.django_db
    def test_validate_prefilledcode_valid_question_match(self, create_prefilledcode_list):
    
        # Arrange
        question_id = 1
        list_of_prefilledcode_ids = [1,2]
        storage = PrefilledCodeStorageImplementation()
    
        # Act
        storage.validate_question_prefilledcode_match( \
            question_id=question_id,
            list_of_prefilledcode_ids=list_of_prefilledcode_ids)
