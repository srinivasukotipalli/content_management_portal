# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "solution_approach_creation_and_updation"
REQUEST_METHOD = "post"
URL_SUFFIX = "question/{question_id}/solution_approach/v1/"

from .test_case_01 import TestCase01SolutionApproachCreationAndUpdationAPITestCase

__all__ = [
    "TestCase01SolutionApproachCreationAndUpdationAPITestCase"
]
