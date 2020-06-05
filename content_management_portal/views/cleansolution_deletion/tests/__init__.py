# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "cleansolution_deletion"
REQUEST_METHOD = "delete"
URL_SUFFIX = "question/{question_id}/cleansolution/{cleansolution_id}/delete/cleansolution/v1/"

from .test_case_01 import TestCase01CleansolutionDeletionAPITestCase

__all__ = [
    "TestCase01CleansolutionDeletionAPITestCase"
]
