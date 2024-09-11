import pytest
from business.services.user_service import UserService
from business.endpoints.enpoint_user import EndpointUser
from business.tools.assertion_manager import AssertionManager


@pytest.mark.deleteuser
def test_delete_user_with_valid_id_returns_200(setup_user):
    user = setup_user
    url = EndpointUser.get_user_id(user['id'])
    response = UserService.delete_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_response_is_true(response)


@pytest.mark.deleteuser
def test_delete_user_with_nonexistent_id_returns_404():
    url = EndpointUser.get_user_id('invalid')
    response = UserService.delete_user(url)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.deleteuser
def test_delete_user_unauthenticated_user_returns_401(setup_user, teardown_user):
    created_user = teardown_user
    user = setup_user
    url = EndpointUser.get_user_id(user['id'])
    response = UserService.delete_user(url, "invalid_user")
    created_user.append(user)
    AssertionManager.assert_status_code_401(response)


@pytest.mark.deleteuser
def test_delete_user_without_permissions_returns_403(setup_user, teardown_user):
    created_user = teardown_user
    user = setup_user
    url = EndpointUser.get_user_id(user['id'])
    response = UserService.delete_user(url, "no_users_access_user")
    created_user.append(user)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.deleteuser
def test_delete_already_deleted_user_returns_404(setup_user):
    user = setup_user
    url = EndpointUser.get_user_id(user['id'])
    response = UserService.delete_user(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_response_is_true(response)
    response2 = UserService.delete_user(url)
    AssertionManager.assert_status_code_404(response2)
