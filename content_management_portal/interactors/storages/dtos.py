from dataclasses import dataclass
from typing import Optional, List
from content_management_portal.constants.enums import (
    TextType,
    CodeLanguage
    )

@dataclass()
class AccessTokenDto:
    access_token: str
    refresh_token: str
    expires_in: int

@dataclass()
class QuestionDto:
    user_id: int
    question_id: Optional[int]
    short_title: str
    content_type: TextType
    content: str

@dataclass()
class RoughSolutionDto:
    code_type: CodeLanguage
    code: str
    filename: str
    roughsolution_id:Optional[int]
    question_id: int

@dataclass()
class PrefilledCodeDto:
    code_type: CodeLanguage
    code: str
    filename: str
    prefilledcode_id:Optional[int]
    question_id: int

@dataclass()
class CleanSolutionDto:
    code_type: CodeLanguage
    code: str
    filename: str
    cleansolution_id:Optional[int]
    question_id: int

@dataclass()
class TestCaseDto:
    order_id: Optional[int]
    input: int
    output: int
    is_hidden: bool
    score: int
    testcase_id:Optional[int]
    question_id: int


@dataclass()
class HintDto:
    title: str
    content_type: TextType
    content: str
    order_id: Optional[int]
    hint_id: Optional[int]
    question_id: int

@dataclass()
class SolutionApproachDto:
    title: str
    description_content_type: TextType
    description_content: str
    complexity_analysis_content_type: TextType
    complexity_analysis_content: str
    question_id: int
    solutionapproach_id: Optional[int]

@dataclass()
class QuestionDetailsDto:
    question_id: int
    short_title: int
    roughsolution: bool
    testcase:bool
    prefilledcode:bool
    solutionapproach:bool
    cleansolution:bool
    hint:bool

@dataclass
class SwapTestCaseDto:
    first_testcase_id: int
    second_testcase_id: int
    first_testcase_number: int
    second_testcase_number: int

@dataclass
class SwapHintDto:
    first_hint_id: int
    second_hint_id: int
    first_hint_number: int
    second_hint_number: int
