from content_management_portal.interactors.storages.storage_interface import \
    StorageInterface
from content_management_portal.interactors.presenters. \
    roughsolution_presenter_interface import PresenterInterface
from content_management_portal.constants.enums import CodeLanguage
from content_management_portal.exceptions import (
    InvalidRoughSolutionId,
    InvalidQuestionId,
    InvalidRoughSolutionForQuestion,
    )
from typing import Optional, List, Dict
from content_management_portal.interactors.storages.dtos \
    import QuestionDto,RoughSolutionDto


class RoughSolutionCreateOrUpdateInteractor:

    def __init__(self, storage: StorageInterface, \
            presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def rough_solution_create_or_update(self, \
            question_id: int,question_rough_solutions_list:List[Dict]):

        try:
            self.storage.validate_question_id(question_id=question_id)
        except InvalidQuestionId:
            self.presenter.raise_invalid_question_exception()

        updated_rough_solutions = []
        created_rough_solutions = []
        list_of_rough_solutions_ids = []

        for roughsolution in question_rough_solutions_list:
            roughsolution_id = roughsolution.get('roughsolution_id')
            if roughsolution_id:
                updated_rough_solutions.append(roughsolution)
                list_of_rough_solutions_ids.append(roughsolution_id)
            else:
                created_rough_solutions.append(roughsolution)

        #print(created_rough_solutions,updated_rough_solutions)

        try:
            self.storage.validate_rough_solution_ids( \
                list_of_rough_solutions_ids=list_of_rough_solutions_ids)
        except InvalidRoughSolutionId:
            self.presenter.raise_invalid_rough_solution_exception()

        try:
            self.storage.validate_question_roughsolutions_match( \
                        question_id=question_id, \
                        list_of_rough_solutions_ids=list_of_rough_solutions_ids)
        except InvalidRoughSolutionForQuestion:
            self.presenter.raise_invalid_rough_solution_for_question_exception()

        created_rough_solutions_dtos = [
                                RoughSolutionDto(
                                    roughsolution_id=None,
                                    code_type=roughsolution["code_type"],
                                    code=roughsolution["code"],
                                    filename=roughsolution["filename"],
                                    question_id=question_id
                                    )
                                    for roughsolution in created_rough_solutions
                                ]

        updated_rough_solutions_dtos = [
                                RoughSolutionDto(
                                    code_type=roughsolution["code_type"],
                                    code=roughsolution["code"],
                                    filename=roughsolution["filename"],
                                    roughsolution_id=roughsolution["roughsolution_id"],
                                    question_id=question_id
                                    )
                                    for roughsolution in updated_rough_solutions
                                ]


        list_of_rough_solutions_dtos = \
                self.storage.updation_and_creation_of_rough_solutions( \
                        question_id=question_id,
                        updated_rough_solutions_dtos=updated_rough_solutions_dtos,
                        created_rough_solutions_dtos=created_rough_solutions_dtos
                        )

        return self.presenter.get_response_for_list_of_rough_solutions_dtos(
                    list_of_rough_solution_dtos=list_of_rough_solutions_dtos
                    )
