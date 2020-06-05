from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.exceptions import (
    InvalidRoughSolutionId,
    InvalidQuestionId,
    InvalidRoughSolutionForQuestion,
    )
from typing import Optional, List, Dict

class RoughSolutionCreateOrUpdateInteractor:

    def __init__(self, storage: StorageInterface, \
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def rough_solution_create_or_update(self, \
            question_id: Optional[int],question_rough_solutions_list:List[Dict]):

        if question_id:
            try:
                self.storage.validate_question_id( \
                    question_id=question_id)
            except InvalidQuestionId:
                self.presenter.raise_invalid_question_exception()


        list_of_rough_solutions_ids = [roughsolution['roughsolution_id'] \
                    for roughsolution in question_rough_solutions_list]
            
        try:
            self.storage.validate_rough_solutions_ids(list_of_rough_solutions_ids)
        except InvalidRoughSolutionId:
            self.presenter.raise_invalid_rough_solution_exception()

        try:
            self.storage.validate_question_roughsolution_match( \
                        question_id=question_id,
                    list_of_rough_solutions_ids = list_of_rough_solutions_ids)
        except InvalidRoughSolutionForQuestion:
            self.presenter.raise_invalid_rough_solution_for_question_exception()

        if question_id:
            list_of_rough_solution_dtos = self.storage.rough_solution_update( \
                question_id=question_id,
                question_rough_solutions_list=question_rough_solutions_list)
            return self.presenter.response_for_list_of_rough_solution_dtos(
                    list_of_rough_solution_dtos=list_of_rough_solution_dtos
                    )
        else:
            list_of_rough_solution_dtos = self.storage.rough_solution_create( \
                question_rough_solutions_list=question_rough_solutions_list)
            return self.presenter.response_for_list_of_rough_solution_dtos(
                    list_of_rough_solution_dtos=list_of_rough_solution_dtos
                    )
