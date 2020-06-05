# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "roughsolution_deletion"
REQUEST_METHOD = "delete"
URL_SUFFIX = "question/{question_id}/roughsolution/{roughsolution_id}/delete/roughsolution/v1/"

from .test_case_01 import TestCase01RoughsolutionDeletionAPITestCase

__all__ = [
    "TestCase01RoughsolutionDeletionAPITestCase"
]
