# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "question_creation"
REQUEST_METHOD = "post"
URL_SUFFIX = "question/v1/"

from .test_case_01 import TestCase01QuestionCreationAPITestCase

__all__ = [
    "TestCase01QuestionCreationAPITestCase"
]
