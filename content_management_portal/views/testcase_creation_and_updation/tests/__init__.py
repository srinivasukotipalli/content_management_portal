# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "testcase_creation_and_updation"
REQUEST_METHOD = "post"
URL_SUFFIX = "question/{question_id}/testcase/v1/"

from .test_case_01 import TestCase01TestcaseCreationAndUpdationAPITestCase

__all__ = [
    "TestCase01TestcaseCreationAndUpdationAPITestCase"
]
