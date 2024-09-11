import pytest
from business.services.user_service import UserService
from business.endpoints.enpoint_user import EndpointUser
from business.tools.assertion_manager import AssertionManager


@pytest.mark.viewuser
def test_get_user_with_valid_id_returns_200(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_user_id(user['id'])
    response = UserService.view_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "id", user['id'])


@pytest.mark.viewuser
def test_get_user_with_nonexistent_id_returns_404():
    url = EndpointUser.get_user_id('invalid')
    response = UserService.view_user(url)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.viewuser
def test_get_user_unauthenticated_returns_401(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_user_id(user['id'])
    response = UserService.view_user(url, "invalid_user")
    AssertionManager.assert_status_code_401(response)


@pytest.mark.viewuser
def test_get_user_without_permission_returns_403(setup_teardown_user):
    user = setup_teardown_user
    url = EndpointUser.get_user_id(user['id'])
    response = UserService.view_user(url, "no_team_access_user")
    AssertionManager.assert_status_code_403(response)


@pytest.mark.viewuser
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_get_deleted_user_returns_404(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    UserService.delete_user(url)
    response = UserService.view_user(url)
    AssertionManager.assert_status_code_404(response)
