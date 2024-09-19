import pytest
import json
from business.services.user_service import UserService
from business.endpoints.enpoint_user import EndpointUser
from business.tools.assertion_manager import AssertionManager
from data.user import create_user_data


@pytest.mark.updateuser
def test_update_user_with_all_required_and_valid_values_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(user_type="regular", is_active=False, user_name="ben_crack", salutation_name="Mr.",
                            first_name="Darwin", last_name="Garcia", send_access_info=False)
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "type", "regular")
    AssertionManager.assert_field_value(response, "isActive", False)
    AssertionManager.assert_field_value(response, "userName", "ben_crack")
    AssertionManager.assert_field_value(response, "salutationName", "Mr.")
    AssertionManager.assert_field_value(response, "firstName", "Darwin")
    AssertionManager.assert_field_value(response, "lastName", "Garcia")


@pytest.mark.updateuser
def test_update_user_with_invalid_user_name_length_or_characters_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(user_name="a" * 101)
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_last_name_exceeding_100_characters_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(last_name="a" * 101)
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_invalid_email_address_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(email_address="invalid-email")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_invalid_teams_ids_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(teams_ids="invalid-format")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_invalid_roles_ids_returns_403(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(roles_ids=["59173389930", "5917338sd9930"])
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.updateuser
def test_update_user_with_invalid_working_time_calendar_id_returns_403(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(working_time_calendar_id="invalid")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.updateuser
def test_update_user_with_invalid_layout_set_id_returns_403(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(layout_set_id="invalid")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.updateuser
def test_update_user_with_nonexistent_user_id_returns_404():
    url = EndpointUser.get_user_id("nonexistent_id")
    data = create_user_data()
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.updateuser
def test_update_user_with_specified_password_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(password="validPassword123")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
