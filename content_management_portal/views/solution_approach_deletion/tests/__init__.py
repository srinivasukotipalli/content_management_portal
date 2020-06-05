# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "solution_approach_deletion"
REQUEST_METHOD = "delete"
URL_SUFFIX = "question/{question_id}/solution_approach/{solution_approach_id}/delete/v1/"

from .test_case_01 import TestCase01SolutionApproachDeletionAPITestCase

__all__ = [
    "TestCase01SolutionApproachDeletionAPITestCase"
]
