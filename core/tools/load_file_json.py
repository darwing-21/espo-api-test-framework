from __future__ import annotations
import json
from pathlib import Path

BASE = Path(__file__).absolute().parent.parent.parent


def resources_schemas_path(path):
    return BASE / "config" / "schemas" / path


def load_schema_resource(filename):
    try:
        with resources_schemas_path(filename).open() as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Schema file '{filename}' not found")


def resources_credential_path(path):
    return BASE / "config" / path


def load_credential_config(filename):
    try:
        with resources_credential_path(filename).open() as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Credential file '{filename}' not found")
    except json.JSONDecodeError as err:
        raise ValueError(f"Failed to decode JSON file '{filename}': {err}")
