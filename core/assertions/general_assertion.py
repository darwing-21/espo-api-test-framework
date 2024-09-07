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

    @staticmethod
    def assert_field_in_list(response, field_name):
        try:
            response_json = response.json()
            items = response_json.get('list', [])
            logger.info(f"Validating each item in 'list' contains the field '{field_name}'.")

            for item in items:
                if field_name not in item:
                    pytest.fail(f"Field '{field_name}' is missing in an item: {item}")
            logger.info(f"All items in 'list' contain the field '{field_name}'.")
        except ValueError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)

    @staticmethod
    def assert_field_not_in_list(response, field_name):
        try:
            response_json = response.json()
            items = response_json.get('list', [])
            logger.info(f"Validating no item in 'list' contains the field '{field_name}'.")
            for item in items:
                if field_name in item:
                    pytest.fail(f"Field '{field_name}' should not be present in any item, but found in: {item}")
            logger.info(f"No items in 'list' contain the field '{field_name}'.")
        except ValueError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)

    @staticmethod
    def assert_list_size(response, expected_count):
        try:
            response_json = response.json()
            items = response_json.get('list', [])
            actual_count = len(items)

            logger.info(f"Validating list contains {expected_count} items. Found: {actual_count}.")
            assert actual_count == expected_count, f"Expected {expected_count} items, but got {actual_count}."
        except ValueError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)

    @staticmethod
    def assert_list_order_ascending(response, field):
        try:
            response_json = response.json()
            items = response_json.get('list', [])

            values = [item.get(field) for item in items if item.get(field) is not None]
            logger.info(f"Validating list is ordered by '{field}' in ascending order.")
            logger.info(f"Values being validated: {values}")
            assert values == sorted(values), (
                f"Expected list to be ordered by '{field}' in ascending order, but got: {values}."
            )
        except ValueError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)
        except KeyError as err:
            logger.error(f"Field '{field}' not found in some items: {err}")
            pytest.fail(f"Field '{field}' not found in some items: {err}", pytrace=False)

    @staticmethod
    def assert_list_order_descending(response, field):
        try:
            response_json = response.json()
            items = response_json.get('list', [])

            values = [item.get(field) for item in items if item.get(field) is not None]
            logger.info(f"Validating list is ordered by '{field}' in descending order.")
            logger.info(f"Values being validated: {values}")
            assert values == sorted(values, reverse=True), (
                f"Expected list to be ordered by '{field}' in descending order, but got: {values}."
            )
        except ValueError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)
        except KeyError as err:
            logger.error(f"Field '{field}' not found in some items: {err}")
            pytest.fail(f"Field '{field}' not found in some items: {err}", pytrace=False)

    @staticmethod
    def assert_field_value(response, field, expected_value):
        try:
            response_json = response.json()
            actual_value = response_json.get(field)
            logger.info(f"Validating field '{field}'. Expected: '{expected_value}', Found: '{actual_value}'.")
            assert actual_value == expected_value, f"Expected '{field}' to be '{expected_value}', but got '{actual_value}'."
        except ValueError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)

    @staticmethod
    def assert_response_text_empty(response):
        try:
            response_text = response.text
            logger.info("Validating that the response text is empty.")
            assert response_text == "", f"Expected response text to be empty, but got '{response_text}'."
        except Exception as err:
            logger.error(f"Failed to validate response text: {err}")
            pytest.fail(f"Failed to validate response text: {err}", pytrace=False)

    @staticmethod
    def assert_list_field_contains(response, field, expected_items):
        try:
            response_json = response.json()
            actual_list = response_json.get(field, [])
            logger.info(
                f"Validating list field '{field}' contains expected items: {expected_items}. Found: {actual_list}.")
            for item in expected_items:
                assert item in actual_list, f"Expected '{field}' to contain item '{item}', but it was not found in {actual_list}."
            unexpected_items = [item for item in actual_list if item not in expected_items]
            assert not unexpected_items, f"Found unexpected items in '{field}': {unexpected_items}. Expected only {expected_items}."
        except ValueError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)

    @staticmethod
    def assert_field_is_null(response, field):
        try:
            response_json = response.json()
            actual_value = response_json.get(field)

            logger.info(f"Validating field '{field}' is null. Found: '{actual_value}'.")
            assert actual_value is None, f"Expected '{field}' to be null, but got '{actual_value}'."
        except ValueError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)
