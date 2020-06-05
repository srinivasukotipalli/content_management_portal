# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "get_question"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/question/{question_id}/v1/"

from .test_case_01 import TestCase01GetQuestionAPITestCase

__all__ = [
    "TestCase01GetQuestionAPITestCase"
]
