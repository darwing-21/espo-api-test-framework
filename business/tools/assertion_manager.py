from core.assertions.schema_assertion import SchemaAssertion
from core.assertions.status_code_assertion import StatusCodeAssertion
from core.assertions.general_assertion import ContentAssertion


class AssertionManager(SchemaAssertion, StatusCodeAssertion, ContentAssertion):
    pass
