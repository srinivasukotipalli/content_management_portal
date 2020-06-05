import pytest
from content_management_portal.constants.enums import TextType
from content_management_portal.interactors.storages.dtos import \
    ( RoughSolutionDto,
        QuestionDto,
        QuestionDetailsDto,
        TestCaseDto,
        PrefilledCodeDto,
        CleanSolutionDto,
        HintDto,
        SolutionApproachDto,
        SwapTestCaseDto,
        SwapHintDto
    )
from content_management_portal.models import \
    (
        Question, 
        User, 
        RoughSolution, 
        Case, 
        PrefilledCode,
        CleanSolution,
        Hint,
        SolutionApproach
    )

@pytest.fixture()
def question_dtos():
    question_dtos = QuestionDto(
            question_id=None,
            short_title="even",
            content_type="HTML",
            content="helloworld",
            user_id=1
        )

    return question_dtos

@pytest.fixture()
def create_user():
    user = User(username="srinu")
    user.set_password("1234")
    user.save()
    return user


@pytest.fixture()
def create_question(create_user):
    question_obj = Question.objects.create(
                                            short_title="even",
                                            content_type="HTML",
                                            content="helloworld",
                                            user_id=1
                                        )
    return question_obj
    

@pytest.fixture()
def question_id_dtos(create_question):
    question_dtos = QuestionDto(
            question_id=1,
            short_title="even",
            content_type="HTML",
            content="helloworld",
            user_id=1
        )

    return question_dtos

@pytest.fixture()
def rough_solution_dto():
    rough_solution_dto = RoughSolutionDto(
            code_type="PYTHON",
            code="str",
            filename="str",
            roughsolution_id=None,
            question_id=1
            )

    return rough_solution_dto
    


@pytest.fixture()
def rough_solution_id_dto():
    rough_solution_id_dto = RoughSolutionDto(
            code_type="PYTHON",
            code="str",
            filename="str",
            roughsolution_id=1,
            question_id=1
            )

    return rough_solution_id_dto


@pytest.fixture()
def create_roughsolution(create_question):
    RoughSolution.objects.create(
            code_type="PYTHON",
            code="str",
            filename="str",
            question_id=1)


@pytest.fixture()
def create_roughsolution_list(create_question):
    RoughSolution.objects.bulk_create( \
        [RoughSolution(code_type="PYTHON",
                        code="str",
                        filename="str",
                        question_id=1),
                                    
        RoughSolution(
                    code_type="C",
                    code="str",
                    filename="str",
                    question_id=1),
        ])


@pytest.fixture()
def create_prefilledcode(create_question):
    PrefilledCode.objects.create(
            code_type="PYTHON",
            code="str",
            filename="str",
            question_id=1)


@pytest.fixture()
def create_prefilledcode_list(create_question):
    PrefilledCode.objects.bulk_create( \
        [PrefilledCode(code_type="PYTHON",
                        code="str",
                        filename="str",
                        question_id=1),
                                    
        PrefilledCode(
                    code_type="C",
                    code="str",
                    filename="str",
                    question_id=1),
        ])
        

@pytest.fixture()
def prefilledcodedto():
    prefilledcodedto = PrefilledCodeDto(
            code_type="PYTHON",
            code="str",
            filename="str",
            prefilledcode_id=None,
            question_id=1
            )

    return prefilledcodedto

@pytest.fixture()
def prefilledcodeiddto():
    prefilledcode_id_dto = PrefilledCodeDto(
                                        code_type="PYTHON",
                                        code="str",
                                        filename="str",
                                        prefilledcode_id=1,
                                        question_id=1
                                        )

    return prefilledcode_id_dto



@pytest.fixture()
def create_cleansolution(create_question):
    CleanSolution.objects.create(
            code_type="PYTHON",
            code="str",
            filename="str",
            question_id=1)


@pytest.fixture()
def create_cleansolution_list(create_question):
    CleanSolution.objects.bulk_create( \
        [CleanSolution(code_type="PYTHON",
                        code="str",
                        filename="str",
                        question_id=1),
                                    
        CleanSolution(
                    code_type="C",
                    code="str",
                    filename="str",
                    question_id=1),
        ])
        

@pytest.fixture()
def cleansolutiondto():
    cleansolutiondto = CleanSolutionDto(
            code_type="PYTHON",
            code="str",
            filename="str",
            cleansolution_id=None,
            question_id=1
            )

    return cleansolutiondto

@pytest.fixture()
def cleansolutioniddto():
    cleansolution_id_dto = CleanSolutionDto(
                                        code_type="PYTHON",
                                        code="str",
                                        filename="str",
                                        cleansolution_id=1,
                                        question_id=1
                                        )

    return cleansolution_id_dto


@pytest.fixture()
def total_questions_dtos_list():
    total_questions_dtos_list = [QuestionDetailsDto(
                                    question_id=1,
                                    short_title= "even",
                                    roughsolution=True,
                                    hint= False,
                                    testcase=False,
                                    prefilledcode=False,
                                    solutionapproach= False,
                                    cleansolution= False)]
    return total_questions_dtos_list


@pytest.fixture()
def testcase_dto(create_question):
    question_obj = create_question
    testcasedto = TestCaseDto(
                                order_id=1,
                                testcase_id=1,
                                input="string",
                                output="string",
                                is_hidden=True,
                                score=1,
                                question_id=question_obj.id
                            )
    return testcasedto
    
@pytest.fixture()
def create_testcase(create_question):
    question_obj = create_question
    testcase_obj = Case(
                            order_id=1,
                            input="string",
                            output="string",
                            is_hidden=True,
                            score=1,
                            question_id=question_obj.id
                            )
    testcase_obj.save()
    return testcase_obj

@pytest.fixture()
def hint_dto(create_question):
    question_obj = create_question
    hintdto = HintDto(
                        hint_id=1,
                        title="string",
                        content_type=TextType.html.value,
                        content="string",
                        order_id=1,
                        question_id=question_obj.id
                    )
    return hintdto
    
@pytest.fixture()
def create_hint(create_question):
    question_obj = create_question
    hint_obj = Hint(
                    title="string",
                    content_type=TextType.html.value,
                    content="string",
                    order_id=1,
                    question_id=question_obj.id
                    )
    hint_obj.save()
    return hint_obj


@pytest.fixture()
def solutionapproach_dto(create_question):
    question_obj = create_question
    solutionapproach_dto = SolutionApproachDto(
                        solutionapproach_id=1,
                        title="string",
                        description_content_type=TextType.html.value,
                        description_content="string",
                        complexity_analysis_content_type=TextType.html.value,
                        complexity_analysis_content="string",
                        question_id=question_obj.id
                    )
    return solutionapproach_dto
    
@pytest.fixture()
def create_solutionapproach(create_question):
    question_obj = create_question
    solutionapproach_obj = SolutionApproach(
                    title="string",
                    description_content_type=TextType.html.value,
                    description_content="string",
                    complexity_analysis_content_type=TextType.html.value,
                    complexity_analysis_content="string",
                    question_id=question_obj.id
                    )
    solutionapproach_obj.save()
    return solutionapproach_obj
    


@pytest.fixture()
def create_testcases(create_question):
    list_of_testcase_objs = \
        Case.objects.bulk_create([Case(
                order_id=1,
                input="string",
                output="string",
                is_hidden=True,
                score=1,
                question_id=1
            ),
        Case(
                order_id=2,
                input="string",
                output="string",
                is_hidden=True,
                score=1,
                question_id=1
            )
        ])
    return list_of_testcase_objs

@pytest.fixture()
def swap_testcase_dto(create_testcases):
    
    swap_testcase_dto = SwapTestCaseDto(
                            first_testcase_id=1,
                            second_testcase_id=2,
                            first_testcase_number=1,
                            second_testcase_number=2
                            )
    return swap_testcase_dto

@pytest.fixture()
def create_hints(create_question):
    list_of_hint_objs = \
        Hint.objects.bulk_create( \
            [
            Hint(
                title="string",
                content_type=TextType.html.value,
                content="string",
                order_id=1,
                question_id=1
                ),
            Hint(
                title="string",
                content_type=TextType.html.value,
                content="string",
                order_id=1,
                question_id=1
                )
        ])
    return list_of_hint_objs

@pytest.fixture()
def swap_hint_dto(create_hints):
    
    swap_hint_dto = SwapHintDto(
                            first_hint_id=1,
                            second_hint_id=2,
                            first_hint_number=1,
                            second_hint_number=2
                            )
    return swap_hint_dto
