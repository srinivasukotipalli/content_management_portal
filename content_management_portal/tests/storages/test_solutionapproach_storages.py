import pytest

from content_management_portal.models import Question, SolutionApproach
from content_management_portal.storages.solutionapproach_storage_implementation \
    import SolutionApproachStorageImplementation


class TestSolutionApproach:

    @pytest.mark.django_db
    def test_solutionapproach_creation(self, solutionapproach_dto):
    
        # Arrange
        question_id = 1
        storage = SolutionApproachStorageImplementation()
        actual_solutionapproach_dto = storage.solutionapproach_creation( \
                            question_id=question_id,
                            created_solutionapproach_dto=solutionapproach_dto
                            )
    
        # Act
        assert actual_solutionapproach_dto.solutionapproach_id == \
                                        solutionapproach_dto.solutionapproach_id
        assert actual_solutionapproach_dto.title==solutionapproach_dto.title
        assert actual_solutionapproach_dto.description_content_type== \
                                solutionapproach_dto.description_content_type
        assert actual_solutionapproach_dto.description_content == \
                                solutionapproach_dto.description_content
        assert actual_solutionapproach_dto.complexity_analysis_content_type== \
                        solutionapproach_dto.complexity_analysis_content_type
        assert actual_solutionapproach_dto.complexity_analysis_content == \
                                solutionapproach_dto.complexity_analysis_content
        assert actual_solutionapproach_dto.question_id== \
                                solutionapproach_dto.question_id

    @pytest.mark.django_db
    def test_solutionapproach_updation(self, \
                        create_solutionapproach, solutionapproach_dto):
    
        # Arrange
        question_id = 1
        storage = SolutionApproachStorageImplementation()
        actual_solutionapproach_dto = storage.solutionapproach_updation( \
                                question_id=question_id,
                                updated_solutionapproach_dto=solutionapproach_dto
                                )
    
        # Act
        assert actual_solutionapproach_dto.solutionapproach_id == \
                                        solutionapproach_dto.solutionapproach_id
        assert actual_solutionapproach_dto.title==solutionapproach_dto.title
        assert actual_solutionapproach_dto.description_content_type== \
                                solutionapproach_dto.description_content_type
        assert actual_solutionapproach_dto.description_content == \
                                solutionapproach_dto.description_content
        assert actual_solutionapproach_dto.complexity_analysis_content_type== \
                        solutionapproach_dto.complexity_analysis_content_type
        assert actual_solutionapproach_dto.complexity_analysis_content == \
                                solutionapproach_dto.complexity_analysis_content
        assert actual_solutionapproach_dto.question_id== \
                                solutionapproach_dto.question_id

    @pytest.mark.django_db
    def test_solutionapproach_deletion(self, create_solutionapproach):

        # Arrange
        question_id = 1
        solutionapproach_id = 1
        storage = SolutionApproachStorageImplementation()
        expected_result = False
        
        # Act
        storage.solutionapproach_deletion(
                        question_id=question_id,
                        solutionapproach_id=solutionapproach_id
                        )
                        
        actual_result = SolutionApproach.objects.filter( \
                                question_id=solutionapproach_id, \
                                            id=solutionapproach_id).exists()
        
        # Arrange
        assert expected_result == actual_result
        
    @pytest.mark.django_db
    def test_validate_question_solutionapproach_match(self, \
                                            create_solutionapproach):
        # Arrange
        question_id = 1
        solutionapproach_id = 1
        storage = SolutionApproachStorageImplementation()
        expected_result = True
        
        # Act
        actual_result = storage.validate_question_solutionapproach_match(
                        question_id=question_id,
                        solutionapproach_id=solutionapproach_id
                        )
                        
        # Arrange
        assert expected_result == actual_result
    
    @pytest.mark.django_db
    def test_validate_solutionapproach_id(self, create_solutionapproach):
        
        # Arrange
        solutionapproach_id = 1
        storage = SolutionApproachStorageImplementation()
        expected_result = True
        
        # Act
        actual_result = storage.validate_solutionapproach_id( \
                                    solutionapproach_id=solutionapproach_id)
                        
        # Arrange
        assert expected_result == actual_result
    
    @pytest.mark.django_db
    def test_validate_question_id(self, create_question):
        
        # Arrange
        question_id = 1
        storage = SolutionApproachStorageImplementation()
        expected_result = None
        
        # Act
        actual_result = storage.validate_question_id(question_id=question_id)
                        
        # Arrange
        assert expected_result == actual_result
    
    