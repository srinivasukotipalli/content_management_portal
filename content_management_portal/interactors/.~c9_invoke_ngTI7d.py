from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.exceptions import (
    InvalidRoughSolutionId,
    InvalidQuestionId
    )


class RoughSolutionCreateOrUpdateInteractor:

    def __init__(self, storage: StorageInterface, \
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def rough_solution_create_or_update(self,question_id: ,question_rough_solutions_list):

        for roughsolution in question_rough_solutions_list:
            try:
                self.storage.validate_rough_solution_id( \
                    roughsolution_id=roughsolution['rough_solution_id'])
            except InvalidRoughSolutionId:
                self.presenter.raise_invalid_rough_solution_exception()
                
            try:
                self.storage.validate_question_roughsolution_match(question_id=)
        
        
        roughsolution_dtos_list= self.storage.rough_solution_create(
                code_type=code_type,
                code=code, 
                filename=filename,
                question_id=question_id
                )
        return self.presenter.get_response_for_rough_solution_list_dto( \
                roughsolution_dto_list=roughsolution_dtos_list)
