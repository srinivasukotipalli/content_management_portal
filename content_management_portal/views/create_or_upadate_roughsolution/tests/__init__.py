# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "create_or_upadate_roughsolution"
REQUEST_METHOD = "post"
URL_SUFFIX = "question/{question_id}/roughsolution/v1/"

from .test_case_01 import TestCase01CreateOrUpadateRoughsolutionAPITestCase

__all__ = [
    "TestCase01CreateOrUpadateRoughsolutionAPITestCase"
]
