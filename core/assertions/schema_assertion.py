from core.tools.load_file_json import load_schema_resource
from core.tools.my_logger import setup_logger
import pytest
from jsonschema import validate, exceptions as jsonschema_exceptions
import json

logger = setup_logger('schema_assertion')


class SchemaAssertion:

    @staticmethod
    def _load_and_validate_schema(response_json, category, schema_file):
        try:
            schema = load_schema_resource(category, schema_file)
            logger.info(f"Loaded schema: {schema_file}")
        except FileNotFoundError:
            logger.error(f"Schema file '{schema_file}' not found")
            pytest.fail(f"Schema file '{schema_file}' not found", pytrace=False)
        except json.JSONDecodeError as err:
            logger.error(f"Failed to decode JSON schema: {err}")
            pytest.fail(f"Failed to decode JSON schema: {err}", pytrace=False)

        try:
            validate(instance=response_json, schema=schema)
            logger.info(f"JSON schema validation for '{schema_file}' passed.")
            return True
        except jsonschema_exceptions.ValidationError as err:
            logger.error(f"JSON schema validation failed: {err.message}\n"
                         f"Path: {err.path}\nSchema Path: {err.schema_path}")
            pytest.fail(f"JSON schema validation failed: {err.message}\n"
                        f"Path: {err.path}\nSchema Path: {err.schema_path}", pytrace=False)
        except jsonschema_exceptions.SchemaError as err:
            logger.error(f"Invalid JSON schema: {err.message}")
            pytest.fail(f"Invalid JSON schema: {err.message}", pytrace=False)

    @staticmethod
    def _validate_response_json(response, schema_file, category):
        try:
            response_json = response.json()
            logger.info(f"Validating response JSON against '{schema_file}'")
        except json.JSONDecodeError as err:
            logger.error(f"Failed to decode response JSON: {err}")
            pytest.fail(f"Failed to decode response JSON: {err}", pytrace=False)
        return SchemaAssertion._load_and_validate_schema(response_json, category, schema_file)

    @staticmethod
    def assert_list_team_schema_file(response):
        return SchemaAssertion._validate_response_json(response, "list_schema.json", "team")

    @staticmethod
    def assert_list_select_team_schema_file(response):
        return SchemaAssertion._validate_response_json(response, "list_select_schema.json", "team")

    @staticmethod
    def assert_create_team_schema_file(response):
        return SchemaAssertion._validate_response_json(response, "create_team_schema.json", "team")

    @staticmethod
    def assert_team_general_schema_file(response):
        return SchemaAssertion._validate_response_json(response, "team_general_schema.json", "team")
