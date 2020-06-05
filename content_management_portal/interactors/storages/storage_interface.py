from abc import abstractmethod
from typing import Optional,List, Dict
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )
from content_management_portal.interactors.storages.dtos \
    import (
            QuestionDto,
            RoughSolutionDto,
            QuestionDetailsDto,
            TestCaseDto,
            PrefilledCodeDto,
            CleanSolutionDto,
            HintDto,
            SolutionApproachDto,
            SwapTestCaseDto,
            SwapHintDto
            )



class StorageInterface:
    
    @abstractmethod
    def is_valid_offset_value(self, offset):
        pass
        
    @abstractmethod
    def is_valid_limit_value(self, limit):
        pass
        
    @abstractmethod
    def get_question_details(self, offset: int, limit: int):
        pass

    @abstractmethod
    def validate_username(self, username: str)->int:
        pass

    @abstractmethod
    def validate_password(self,username=str, password=str):
        pass

    @abstractmethod
    def question_creation(self, \
                user_id: int,
                short_title: str,
                content_type:TextType,
                content:str) -> QuestionDto:
                pass

    @abstractmethod
    def question_updation(self, \
                user_id: int,
                short_title: str,
                content_type:TextType,
                content:str,
                question_id:int) -> QuestionDto:
                pass

    @abstractmethod
    def question_deletion(self,question_id:int):
        pass

    @abstractmethod
    def validate_question_id(self,question_id: int):
        pass

    @abstractmethod
    def validate_rough_solution_ids(self, \
            list_of_rough_solutions_ids: List[int]):
        pass

    @abstractmethod
    def validate_question_roughsolutions_match(self, \
                        question_id: int,
                        list_of_rough_solutions_ids: List[int]
                        ):
                            pass

    @abstractmethod
    def updation_and_creation_of_rough_solutions(self,question_id:int, \
                updated_rough_solutions_dtos:List[RoughSolutionDto],
                created_rough_solutions_dtos:List[RoughSolutionDto]
                )->List[RoughSolutionDto]:
                    pass

    @abstractmethod
    def rough_solution_deletion(self,question_id:int,rough_solution_id:int):
        pass

    @abstractmethod
    def validate_testcase_id(self,testcase_id: int)->bool:
        pass

    @abstractmethod
    def validate_question_testcase_match(self, question_id: int, \
                            testcase_id: int)->bool:
                            pass

    @abstractmethod
    def testcase_updation(self, question_id: int, \
                            updated_testcase_dto: TestCaseDto)->TestCaseDto:
                            pass
    
    @abstractmethod
    def testcase_creation(self, question_id: int, \
                            created_testcase_dto: TestCaseDto)->TestCaseDto:
                            pass
    
    @abstractmethod
    def testcase_deletion(self,question_id:int,testcase_id:int):
        pass
    
    
    @abstractmethod
    def validate_hint_id(self,hint_id: int)->bool:
        pass

    @abstractmethod
    def validate_question_hint_match(self, question_id: int, \
                            hint_id: int)->bool:
                            pass

    @abstractmethod
    def hint_updation(self, question_id: int, \
                            updated_hint_dto: HintDto)->HintDto:
                            pass
    
    @abstractmethod
    def hint_creation(self, question_id: int, \
                            created_hint_dto: HintDto)->HintDto:
                            pass
    
    @abstractmethod
    def hint_deletion(self,question_id:int,hint_id:int):
        pass
    
    @abstractmethod
    def validate_solutionapproach_id(self,solutionapproach_id: int)->bool:
        pass

    @abstractmethod
    def validate_question_solutionapproach_match(self, question_id: int, \
                            solutionapproach_id: int)->bool:
                            pass

    @abstractmethod
    def solutionapproach_updation(self, question_id: int, \
                            updated_solutionapproach_dto: SolutionApproachDto) \
                                    ->SolutionApproachDto:
                            pass
    
    @abstractmethod
    def solutionapproach_creation(self, question_id: int, \
                            created_solutionapproach_dto: SolutionApproachDto) \
                                ->SolutionApproachDto:
                            pass
    
    @abstractmethod
    def solutionapproach_deletion(self,question_id:int,solutionapproach_id:int):
        pass

    @abstractmethod
    def validate_prefilledcode_ids(self, list_of_prefilledcode_ids: List[int]):
        pass
    
    @abstractmethod
    def validate_question_prefilledcode_match(self, \
                        question_id: int,
                        list_of_prefilledcode_ids: List[int]
                        ):
                            pass

    @abstractmethod
    def updation_and_creation_of_prefilledcodes(self,question_id:int, \
                updated_prefilledcode_dtos:List[PrefilledCodeDto],
                created_prefilledcode_dtos:List[PrefilledCodeDto]
                )->List[PrefilledCodeDto]:
                    pass

    @abstractmethod
    def prefilledcode_deletion(self, question_id: int, prefilledcode_id: int):
        pass
    
    @abstractmethod
    def validate_cleansolution_ids(self, list_of_cleansolution_ids: List[int]):
        pass
    
    @abstractmethod
    def validate_question_cleansolution_match(self, \
                        question_id: int,
                        list_of_cleansolution_ids: List[int]
                        ):
                            pass

    @abstractmethod
    def updation_and_creation_of_cleansolutions(self,question_id:int, \
                updated_cleansolution_dtos:List[CleanSolutionDto],
                created_cleansolution_dtos:List[CleanSolutionDto]
                )->List[CleanSolutionDto]:
                    pass

    @abstractmethod
    def cleansolution_deletion(self, question_id: int, cleansolution_id: int):
        pass
    
    @abstractmethod
    def get_question(self, question_id: int):
        pass
    
    @abstractmethod
    def swap_testcase_numbers_for_testcases(self, 
        question_id: int, swap_dto: SwapTestCaseDto) -> SwapTestCaseDto:
        pass

    @abstractmethod
    def validate_question_testcases_match(self, \
        question_id: int, first_testcase_id: int, second_testcase_id: int):
        pass
    
    @abstractmethod
    def validate_testcase_ids(self, 
        first_testcase_id: int, second_testcase_id: int):
            pass
    
    @abstractmethod
    def swap_hint_numbers_for_hints(self, 
        question_id: int, swap_dto: SwapHintDto) -> SwapHintDto:
        pass

    @abstractmethod
    def validate_question_hints_match(self, \
        question_id: int, first_hint_id: int, second_hint_id: int):
        pass
    
    @abstractmethod
    def validate_hint_ids(self, 
        first_hint_id: int, second_hint_id: int):
            pass
