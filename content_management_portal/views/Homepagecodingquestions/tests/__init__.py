# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "Homepagecodingquestions"
REQUEST_METHOD = "get"
URL_SUFFIX = "homepage/codingquestions/v1/"

from .test_case_01 import TestCase01HomepagecodingquestionsAPITestCase

__all__ = [
    "TestCase01HomepagecodingquestionsAPITestCase"
]
