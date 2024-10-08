import pytest
import json
from business.services.user_service import UserService
from business.endpoints.enpoint_user import EndpointUser
from business.tools.assertion_manager import AssertionManager
from data.user import create_user_data


@pytest.mark.createuser
def test_create_user_with_all_required_valid_values_returns_200(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(user_type="regular", is_active=False, user_name="ben_crack", salutation_name="Mr.",
                            first_name="Darwin", last_name="Garcia", send_access_info=False)
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "type", "regular")
    AssertionManager.assert_field_value(response, "isActive", False)
    AssertionManager.assert_field_value(response, "userName", "ben_crack")
    AssertionManager.assert_field_value(response, "salutationName", "Mr.")
    AssertionManager.assert_field_value(response, "firstName", "Darwin")
    AssertionManager.assert_field_value(response, "lastName", "Garcia")
    created_teams.append(response.json())


@pytest.mark.createuser
def test_create_user_with_valid_user_name_length_and_characters_returns_200(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(user_name="username_valid123")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "userName", "username_valid123")


@pytest.mark.createuser
def test_create_user_with_invalid_user_name_length_or_characters_returns_400():
    url = EndpointUser.get_base_user()
    data = create_user_data(user_name="null")
    response = UserService.create_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.createuser
def test_create_user_with_first_name_exceeding_100_characters_returns_400():
    url = EndpointUser.get_base_user()
    data = create_user_data(
        user_name="Johnathon Maximillian Alexanderson Christopher Davidson Benjamin Theodore Jameson Nathaniel Montgomea")
    response = UserService.create_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.createuser
def test_create_user_with_valid_last_name_up_to_100_characters_returns_200(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(
        last_name="Johnathon Maximillian Alexanderson Christopher Davidson Benjamin Theodore Jameson Nathaniel Montgome")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "lastName",
                                        "Johnathon Maximillian Alexanderson Christopher Davidson Benjamin Theodore Jameson Nathaniel Montgome")


@pytest.mark.createuser
def test_create_user_with_last_name_exceeding_100_characters_returns_error():
    url = EndpointUser.get_base_user()
    data = create_user_data(
        last_name="Johnathon Maximillian Alexanderson Christopher Davidson Benjamin Theodore Jameson Nathaniel Montgomea")
    response = UserService.create_user(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.createuser
def test_create_user_with_valid_email_address_returns_200(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(email_address="darwingarcia2124@gmail.com")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "emailAddress", "darwingarcia2124@gmail.com")


@pytest.mark.createuser
def test_create_user_with_valid_phone_number_returns_200(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(phone_number="+59173389930")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "phoneNumber", "+59173389930")


@pytest.mark.createuser
def test_create_user_with_valid_gender_male_female_neutral_returns_200(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(gender="Female")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "gender", "Female")


@pytest.mark.createuser
def test_create_user_with_valid_teams_ids_returns_200(teardown_user, setup_teardown_team_global):
    created_teams = teardown_user
    team = setup_teardown_team_global
    url = EndpointUser.get_base_user()
    data = create_user_data(teams_ids=[team['id']])
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_list_field_contains(response, "teamsIds", [team['id']])


@pytest.mark.createuser
def test_create_user_with_valid_default_team_id_returns_200(teardown_user, setup_teardown_team_global):
    created_teams = teardown_user
    team = setup_teardown_team_global
    url = EndpointUser.get_base_user()
    data = create_user_data(teams_ids=[team['id']], default_team_id=team['id'])
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_list_field_contains(response, "teamsIds", [team['id']])
    AssertionManager.assert_field_value(response, "defaultTeamId", team['id'])


@pytest.mark.createuser
def test_create_user_with_valid_roles_ids_returns_200(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(roles_ids=["6703f64ba26bb589d", "6703f804da5feb1b0"])
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_list_field_contains(response, "rolesIds", ["6703f64ba26bb589d", "6703f804da5feb1b0"])


@pytest.mark.createuser
def test_create_user_with_valid_working_time_calendar_id_returns_200(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(working_time_calendar_id="6703f8ace83cd97ed")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "workingTimeCalendarId", "6703f8ace83cd97ed")


@pytest.mark.createuser
def test_create_user_with_valid_layout_set_id_returns_200(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(layout_set_id="6703f89e1996ee098")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "layoutSetId", "6703f89e1996ee098")


@pytest.mark.createuser
def test_create_user_with_valid_avatar_color_returns_200(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(avatar_color="#FFFFFF")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
    AssertionManager.assert_field_value(response, "avatarColor", "#FFFFFF")


@pytest.mark.createuser
def test_create_user_with_invalid_layout_set_id_returns_400(teardown_user):
    created_teams = teardown_user
    url = EndpointUser.get_base_user()
    data = create_user_data(password="password123")
    AssertionManager.assert_create_user_schema_file(json.loads(data))
    response = UserService.create_user(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_user_general_schema_file(response)
