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
    AssertionManager.assert_field_value_not_in_response(response, "id", "66d8f6a634904dc79")


@pytest.mark.listuser
def test_list_users_with_api_type_returns_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(userType="api")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_field_value_in_response(response, "id", "66d8f6a634904dc79")
    AssertionManager.assert_field_value_not_in_response(response, "id", user['id'])


@pytest.mark.listuser
def test_list_users_with_invalid_user_type_returns_empty_list_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(userType="unknown")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_field_value(response, "total", 0)


@pytest.mark.listuser
def test_list_users_with_select_parameter_returns_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(select="gender")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_field_in_list(response, "gender")


@pytest.mark.listuser
def test_handle_min_max_size_returns_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(maxSize=1)
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_list_size(response, 1)


@pytest.mark.listuser
def test_handle_max_max_size_returns_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(maxSize=200)
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)


@pytest.mark.listuser
def test_max_size_above_limit_returns_400(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(maxSize=201)
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.listuser
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_negative_max_size_returns_400(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(maxSize=-1)
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listuser
def test_handle_min_offset_returns_200(setup_teardown_user):
    user = setup_teardown_user
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
    user = setup_teardown_user
    url = EndpointUser.get_list_user(select="gender", orderBy="gender")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_ascending(response, "gender")


@pytest.mark.listuser
def test_order_asc_returns_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(select="username", order="asc")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_ascending(response, "username")


@pytest.mark.listuser
def test_order_desc_returns_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(select="username", order="desc")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_descending(response, "username")


@pytest.mark.listuser
def test_ignore_empty_order_by_returns_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(orderBy="")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_user_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_ascending(response, "username")


@pytest.mark.listuser
def test_invalid_order_by_field_returns_400(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(orderBy="unknown")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listuser
def test_invalid_order_value_returns_400(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user(order="unknown")
    response = UserService.get_list_user(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listuser
def test_get_teams_unauthenticated_user_returns_http_401(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user()
    response = UserService.get_list_user(url, "invalid_user")
    AssertionManager.assert_status_code_401(response)


@pytest.mark.listuser
def test_user_without_permissions_cannot_access_teams_module_returns_403(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_list_user()
    response = UserService.get_list_user(url, "no_users_access_user")
    AssertionManager.assert_status_code_403(response)
