# pylint: disable=wrong-import-position

APP_NAME = "content_management_portal"
OPERATION_NAME = "swap_testcase_order_id"
REQUEST_METHOD = "put"
URL_SUFFIX = "swap_testcase_orders/question/{question_id}/v1/"

from .test_case_01 import TestCase01SwapTestcaseOrderIdAPITestCase

__all__ = [
    "TestCase01SwapTestcaseOrderIdAPITestCase"
]
