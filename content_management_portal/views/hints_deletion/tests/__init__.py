# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "hints_deletion"
REQUEST_METHOD = "delete"
URL_SUFFIX = "question/{question_id}/hint/{hint_id}/delete/v1/"

from .test_case_01 import TestCase01HintsDeletionAPITestCase

__all__ = [
    "TestCase01HintsDeletionAPITestCase"
]
