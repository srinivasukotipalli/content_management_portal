# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "question_updation"
REQUEST_METHOD = "post"
URL_SUFFIX = "question/{question_id}/v1/"

from .test_case_01 import TestCase01QuestionUpdationAPITestCase

__all__ = [
    "TestCase01QuestionUpdationAPITestCase"
]
