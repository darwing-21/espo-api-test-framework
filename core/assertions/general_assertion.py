from core.tools.my_logger import setup_logger
import pytest

logger = setup_logger('content_assertion')


class ContentAssertion:
    @staticmethod
    def assert_total_greater_than_zero(response):
        try:
            response_json = response.json()
            total = response_json.get('total', 0)
            logger.info(f"Validating 'total' is greater than 0. Found: {total}")
            assert total > 0, f"Expected 'total' to be greater than 0, but got {total}."
        except ValueError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)

    @staticmethod
    def assert_list_not_empty(response):
        try:
            response_json = response.json()
            items = response_json.get('list', [])
            logger.info(f"Validating 'list' is not empty. Found {len(items)} items.")
            assert len(items) > 0, "Expected 'list' to not be empty, but it is empty."
        except ValueError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)
