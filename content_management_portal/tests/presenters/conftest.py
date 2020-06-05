import pytest
from content_management_portal.interactors.storages.dtos import \
    (
        RoughSolutionDto,
        QuestionDto,
        QuestionDetailsDto,
        TestCaseDto,
        PrefilledCodeDto,
        CleanSolutionDto,
        HintDto,
        SolutionApproachDto
    )
from content_management_portal.constants.enums import TextType


@pytest.fixture
def list_of_rough_solution_dtos():
    rough_solution_dtos = [
                            RoughSolutionDto(
                                                code_type="C",
                                                code="str",
                                                filename="str",
                                                roughsolution_id=1,
                                                question_id= 1
                                            ),
                            
                            RoughSolutionDto(
                                                code_type="PYTHON",
                                                code="str",
                                                filename="str",
                                                roughsolution_id=2,
                                                question_id= 1
                                            ),
                            
                         ]
    return rough_solution_dtos
    
@pytest.fixture
def list_of_prefilledcode_dtos():
    prefilledcode_dtos = [
                            PrefilledCodeDto(
                                                code_type="C",
                                                code="str",
                                                filename="str",
                                                prefilledcode_id=1,
                                                question_id= 1
                                            ),
                            
                            PrefilledCodeDto(
                                                code_type="PYTHON",
                                                code="str",
                                                filename="str",
                                                prefilledcode_id=2,
                                                question_id= 1
                                            ),
                            
                         ]
    return prefilledcode_dtos


@pytest.fixture
def list_of_cleansolution_dtos():
    cleansolution_dtos = [
                            CleanSolutionDto(
                                                code_type="C",
                                                code="str",
                                                filename="str",
                                                cleansolution_id=1,
                                                question_id= 1
                                            ),
                            
                            CleanSolutionDto(
                                                code_type="PYTHON",
                                                code="str",
                                                filename="str",
                                                cleansolution_id=2,
                                                question_id= 1
                                            ),
                            
                         ]
    return cleansolution_dtos
    
@pytest.fixture
def questiondto():
    question_dto =  QuestionDto(
                                    user_id=1,
                                    question_id=1,
                                    short_title="str",
                                    content_type="HTML",
                                    content="str"
                                )
    return question_dto
    
@pytest.fixture()
def total_questions_dtos_list():
    total_questions_dtos_list = [QuestionDetailsDto(
                                    question_id=1,
                                    short_title="even",
                                    roughsolution=True,
                                    hint= False,
                                    testcase=False,
                                    prefilledcode=False,
                                    solutionapproach= False,
                                    cleansolution= False)]
    return total_questions_dtos_list

@pytest.fixture
def testcase_dto():
    testcase_dto =  TestCaseDto(
                                order_id=1,
                                testcase_id=1,
                                input="string",
                                output="string",
                                is_hidden=True,
                                score=1,
                                question_id=1
                                )
    return testcase_dto

@pytest.fixture
def hint_dto():
    hint_dto =  HintDto(
                            hint_id=1,
                            title="string",
                            content_type=TextType.html.value,
                            content="string",
                            order_id=1,
                            question_id=1
                        )
    return hint_dto

@pytest.fixture
def solutionapproach_dto():
    solutionapproach_dto =  SolutionApproachDto(
                            question_id= None,
                            solutionapproach_id=1,
                            title="string",
                            description_content_type=TextType.html.value,
                            description_content="string",
                            complexity_analysis_content_type=TextType.html.value,
                            complexity_analysis_content="string",
                        )
    return solutionapproach_dto
