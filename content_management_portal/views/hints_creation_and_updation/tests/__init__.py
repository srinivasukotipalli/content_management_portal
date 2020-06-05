# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "hints_creation_and_updation"
REQUEST_METHOD = "post"
URL_SUFFIX = "question/{question_id}/hint/v1/"

from .test_case_01 import TestCase01HintsCreationAndUpdationAPITestCase

__all__ = [
    "TestCase01HintsCreationAndUpdationAPITestCase"
]
