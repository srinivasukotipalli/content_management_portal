import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec

from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.storage_interface \
    import StorageInterface
from content_management_portal.interactors.presenters. \
    question_presenter_interface import PresenterInterface
from content_management_portal.interactors.question_creation_interactor \
    import QuestionCreateInteractor
    
class TestQuestionInteractor:
    
    def test_question_create(self,questiondto):
        user_id=1
        short_title="hello"
        content_type="HTML"
        content="hi"
        
        storage=create_autospec(StorageInterface)
        presenter=create_autospec(PresenterInterface)
        
        interactor = QuestionCreateInteractor(storage=storage,presenter=presenter)
        interactor.question_creation(user_id=user_id,short_title=short_title, \
                content_type=content_type, content=content)
                
        # Assert
        storage.question_creation.assert_called_once_with( \
                                                user_id=user_id,
                                                short_title=short_title,
                                                content_type=content_type,
                                                content=content
                                            )
        presenter.get_question_dto_response(questiondto=questiondto)
    def test_question_create(self,questiondto):
        user_id=1
        short_title="hello"
        content_type="HTML"
        content="hi"
        
        storage=create_autospec(StorageInterface)
        presenter=create_autospec(PresenterInterface)
        
        interactor = QuestionCreateInteractor(storage=storage,presenter=presenter)
        interactor.question_creation(user_id=user_id,short_title=short_title, \
                content_type=content_type, content=content)
                
        # Assert
        storage.question_creation.assert_called_once_with( \
                                                user_id=user_id,
                                                short_title=short_title,
                                                content_type=content_type,
                                                content=content
                                            )
        presenter.get_question_dto_response(questiondto=questiondto)
