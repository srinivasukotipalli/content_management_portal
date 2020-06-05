# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "cleansolution_creation_or_updation"
REQUEST_METHOD = "post"
URL_SUFFIX = "question/{question_id}/cleansolution/v1/"

from .test_case_01 import TestCase01CleansolutionCreationOrUpdationAPITestCase

__all__ = [
    "TestCase01CleansolutionCreationOrUpdationAPITestCase"
]
