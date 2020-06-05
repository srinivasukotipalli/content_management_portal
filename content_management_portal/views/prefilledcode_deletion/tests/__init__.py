# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "prefilledcode_deletion"
REQUEST_METHOD = "delete"
URL_SUFFIX = "question/{question_id}/prefilledcode/{prefilledcode_id}/delete/prefilledcode/v1/"

from .test_case_01 import TestCase01PrefilledcodeDeletionAPITestCase

__all__ = [
    "TestCase01PrefilledcodeDeletionAPITestCase"
]
