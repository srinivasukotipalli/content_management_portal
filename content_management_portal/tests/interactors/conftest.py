import pytest

from content_management_portal.constants.enums import TextType,CodeLanguage
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


@pytest.fixture()
def questiondto():
    questiondto = QuestionDto(
                                user_id = 1,
                                short_title = "even",
                        		content_type = TextType.html.value,
                        		content = "helloworld",
                        		question_id = 1
                        		)
    return questiondto

@pytest.fixture()
def roughsolutioniddto():
    roughsolutiondto = RoughSolutionDto(
                                code_type=CodeLanguage.python.value,
                                code="string",
                                filename="string",
                                roughsolution_id=1,
                                question_id=1
                                )
    return roughsolutiondto

@pytest.fixture()
def roughsolutiondto():
    roughsolutiondto = RoughSolutionDto(
                                code_type=CodeLanguage.python.value,
                                code="string",
                                filename="string",
                                roughsolution_id=None,
                                question_id=1
                                )
    return roughsolutiondto

@pytest.fixture()
def prefilledcodeiddto():
    prefilledcodeiddto = PrefilledCodeDto(
                                code_type=CodeLanguage.python.value,
                                code="string",
                                filename="string",
                                prefilledcode_id=1,
                                question_id=1
                                )
    return prefilledcodeiddto

@pytest.fixture()
def prefilledcodedto():
    prefilledcodedto = PrefilledCodeDto(
                                code_type=CodeLanguage.python.value,
                                code="string",
                                filename="string",
                                prefilledcode_id=None,
                                question_id=1
                                )
    return prefilledcodedto

@pytest.fixture()
def cleansolutioniddto():
    cleansolutioniddto = CleanSolutionDto(
                                code_type=CodeLanguage.python.value,
                                code="string",
                                filename="string",
                                cleansolution_id=1,
                                question_id=1
                                )
    return cleansolutioniddto

@pytest.fixture()
def cleansolutiondto():
    cleansolutiondto = CleanSolutionDto(
                                code_type=CodeLanguage.python.value,
                                code="string",
                                filename="string",
                                cleansolution_id=None,
                                question_id=1
                                )
    return cleansolutiondto

@pytest.fixture()
def testcasedto():
    testcasedto = TestCaseDto(
                                order_id=1,
                                input="string",
                                output="string",
                                is_hidden=True,
                                score=1,
                                testcase_id=None,
                                question_id=1
                                )
    return testcasedto

@pytest.fixture()
def testcaseiddto():
    testcaseiddto = TestCaseDto(
                                order_id=1,
                                input="string",
                                output="string",
                                is_hidden=True,
                                score=1,
                                testcase_id=1,
                                question_id=1
                                )
    return testcaseiddto

@pytest.fixture()
def hintdto():
    hintdto = HintDto(
                        title="string",
                        content_type=TextType.html.value,
                        content="string",
                        order_id=1,
                        hint_id=None,
                        question_id=1
                    )
    return hintdto

@pytest.fixture()
def hintiddto():
    hintiddto = HintDto(
                        title="string",
                        content_type=TextType.html.value,
                        content="string",
                        order_id=1,
                        hint_id=1,
                        question_id=1
                    )
    return hintiddto


@pytest.fixture()
def solutionapproachdto():
    solutionapproachdto = SolutionApproachDto(
                        title="string",
                        description_content_type=TextType.html.value,
                        description_content="string",
                        complexity_analysis_content_type=TextType.html.value,
                        complexity_analysis_content="string",
                        solutionapproach_id=None,
                        question_id=1
                    )
    return solutionapproachdto

@pytest.fixture()
def solutionapproachiddto():
    solutionapproachiddto = SolutionApproachDto(
                        title="string",
                        description_content_type=TextType.html.value,
                        description_content="string",
                        complexity_analysis_content_type=TextType.html.value,
                        complexity_analysis_content="string",
                        solutionapproach_id=1,
                        question_id=1
                    )
    return solutionapproachiddto

@pytest.fixture()
def total_questions_dtos_list():
    total_questions_dtos_list = [QuestionDetailsDto(
                                    question_id=1,
                                    short_title= "string",
                                    roughsolution=True,
                                    hint= True,
                                    testcase=True,
                                    prefilledcode=True,
                                    solutionapproach= True,
                                    cleansolution= True)]
    return total_questions_dtos_list


@pytest.fixture()
def swap_testcase_dto():
    
    swap_testcase_dto = SwapTestCaseDto(
                            first_testcase_id=1,
                            second_testcase_id=1,
                            first_testcase_number=1,
                            second_testcase_number=1
                            )
    return swap_testcase_dto

@pytest.fixture()
def swap_hint_dto():
    
    swap_hint_dto = SwapHintDto(
                            first_hint_id=1,
                            second_hint_id=2,
                            first_hint_number=1,
                            second_hint_number=2
                            )
    return swap_testcase_dto
