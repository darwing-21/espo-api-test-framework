import pytest
from business.services.user_service import UserService
from business.endpoints.enpoint_user import EndpointUser
from business.tools.assertion_manager import AssertionManager


@pytest.mark.listuser
def test_list_users_with_internal_type_returns_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(userType="internal")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_field_value_in_response(response, "id", user['id'])
    AssertionManager.assert_field_value_not_in_response(response, "id", "6703f58e9acadd548")


@pytest.mark.listuser
def test_list_users_with_api_type_returns_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(userType="api")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_field_value_in_response(response, "id", "6703f58e9acadd548")
    AssertionManager.assert_field_value_not_in_response(response, "id", user['id'])


@pytest.mark.listuser
def test_list_users_with_select_parameter_returns_200(setup_teardown_user):
    url = EndpointUser.get_list_user(select="gender")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_field_in_list(response, "gender")


@pytest.mark.listuser
def test_handle_max_max_size_returns_200(setup_teardown_user):
    url = EndpointUser.get_list_user(maxSize=200)
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)


@pytest.mark.listuser
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_negative_max_size_returns_400(setup_teardown_user):
    url = EndpointUser.get_list_user(maxSize=-1)
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listuser
def test_handle_min_offset_returns_200(setup_teardown_user):
    url = EndpointUser.get_list_user(offset=0)
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)


@pytest.mark.listuser
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_negative_offset_returns_400(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(offset=-1)
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listuser
def test_order_by_valid_field_returns_200(setup_teardown_user):
    url = EndpointUser.get_list_user(select="gender", orderBy="gender")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_ascending(response, "gender" )
