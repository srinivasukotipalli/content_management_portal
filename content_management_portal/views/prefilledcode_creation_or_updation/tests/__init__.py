# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "prefilledcode_creation_or_updation"
REQUEST_METHOD = "post"
URL_SUFFIX = "question/{question_id}/prefilledcode/v1/"

from .test_case_01 import TestCase01PrefilledcodeCreationOrUpdationAPITestCase

__all__ = [
    "TestCase01PrefilledcodeCreationOrUpdationAPITestCase"
]
