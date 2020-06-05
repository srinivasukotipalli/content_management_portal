# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "testcase_deletion"
REQUEST_METHOD = "delete"
URL_SUFFIX = "question/{question_id}/testcase/{testcase_id}/delete/v1/"

from .test_case_01 import TestCase01TestcaseDeletionAPITestCase

__all__ = [
    "TestCase01TestcaseDeletionAPITestCase"
]
