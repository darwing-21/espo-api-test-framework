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
def test_update_user_with_valid_type_internal_or_api_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(user_type="api")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "type", "api")


@pytest.mark.updateuser
def test_update_user_with_empty_or_undefined_type_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(user_type="unknown")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_is_active_true_or_false_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(is_active=True)
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "isActive", True)


@pytest.mark.updateuser
def test_update_user_with_invalid_or_missing_is_active_defaults_to_false_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(is_active="unknown")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "isActive", False)


@pytest.mark.updateuser
def test_update_user_with_valid_user_name_length_and_characters_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(user_name="username_valid123")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "userName", "username_valid123")


@pytest.mark.updateuser
def test_update_user_with_invalid_user_name_length_or_characters_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(user_name="a" * 101)
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_valid_first_name_up_to_100_characters_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(first_name="a" * 100)
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "firstName", "a" * 100)


@pytest.mark.updateuser
def test_update_user_with_first_name_exceeding_100_characters_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(first_name="a" * 101)
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_valid_last_name_up_to_100_characters_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(last_name="a" * 100)
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "lastName", "a" * 100)


@pytest.mark.updateuser
def test_update_user_with_last_name_exceeding_100_characters_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(last_name="a" * 101)
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_valid_email_address_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(email_address="test@example.com")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "emailAddress", "test@example.com")


@pytest.mark.updateuser
def test_update_user_with_invalid_email_address_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(email_address="invalid-email")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_valid_phone_number_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(phone_number="+59173389930")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "phoneNumber", "+59173389930")


@pytest.mark.updateuser
def test_update_user_with_invalid_phone_number_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(phone_number="+59173")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_valid_gender_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(gender="Male")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "gender", "Male")


@pytest.mark.updateuser
def test_update_user_with_invalid_gender_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(gender="invalid")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_valid_teams_ids_returns_200(setup_teardown_user_function, setup_teardown_team):
    user = setup_teardown_user_function
    team = setup_teardown_team
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(teams_ids=[team['id']])
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_list_field_contains(response, "teamsIds", [team['id']])


@pytest.mark.updateuser
def test_update_user_with_invalid_teams_ids_returns_400(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(teams_ids="invalid-format")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_valid_default_team_id_returns_200(setup_teardown_user_function, setup_teardown_team):
    user = setup_teardown_user_function
    team = setup_teardown_team
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(teams_ids=[team['id']], default_team_id=team['id'])
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "defaultTeamId", team['id'])


@pytest.mark.updateuser
def test_update_user_with_invalid_default_team_id_returns_400(setup_teardown_user_function, setup_teardown_team):
    user = setup_teardown_user_function
    team = setup_teardown_team
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(teams_ids=[team['id']], default_team_id="invalid")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateuser
def test_update_user_with_valid_roles_ids_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(roles_ids=["52bd3ee937361", "52bc41359084d"])
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_list_field_contains(response, "rolesIds", ["52bd3ee937361", "52bc41359084d"])


@pytest.mark.updateuser
def test_update_user_with_invalid_roles_ids_returns_403(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(roles_ids=["59173389930", "5917338sd9930"])
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.updateuser
def test_update_user_with_valid_working_time_calendar_id_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(working_time_calendar_id="66d8f90b424428d1b")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "workingTimeCalendarId", "66d8f90b424428d1b")


@pytest.mark.updateuser
def test_update_user_with_invalid_working_time_calendar_id_returns_403(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(working_time_calendar_id="invalid")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.updateuser
def test_update_user_with_valid_layout_set_id_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(layout_set_id="66d8f8ff4f1c23bca")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "layoutSetId", "66d8f8ff4f1c23bca")


@pytest.mark.updateuser
def test_update_user_with_invalid_layout_set_id_returns_403(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(layout_set_id="invalid")
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.updateuser
def test_update_user_with_specified_password_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(password="validPassword123")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)


@pytest.mark.updateuser
def test_update_user_with_valid_avatar_color_returns_200(setup_teardown_user_function):
    user = setup_teardown_user_function
    url = EndpointUser.get_user_id(user['id'])
    data = create_user_data(avatar_color="#FFFFFF")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "avatarColor", "#FFFFFF")


@pytest.mark.updateuser
def test_update_user_with_nonexistent_user_id_returns_404():
    url = EndpointUser.get_user_id("nonexistent_id")
    data = create_user_data()
    response = UserService.update_user(url, data)
    AssertionManager.assert_status_code_404(response)
