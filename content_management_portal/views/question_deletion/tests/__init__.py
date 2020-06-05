# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "question_deletion"
REQUEST_METHOD = "delete"
URL_SUFFIX = "question/{question_id}/delete/question/v1/"

from .test_case_01 import TestCase01QuestionDeletionAPITestCase

__all__ = [
    "TestCase01QuestionDeletionAPITestCase"
]
