import json
import pytest
from business.endpoints.endpoint_team import EndpointTeams
from business.services.team_service import TeamService
from business.tools.assertion_manager import AssertionManager
from data.team import create_team_data


@pytest.mark.createteam
def test_create_team_with_valid_name_returns_201(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", roles_ids=["6703f64ba26bb589d", "6703f804da5feb1b0"],
                            positions=["Dev", "Qa"],
                            layout_set_id="6703f89e1996ee098", working_time_calendar_id="6703f8ace83cd97ed")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "name", "Team Test QA")
    AssertionManager.assert_list_field_contains(response, "rolesIds", ["6703f64ba26bb589d", "6703f804da5feb1b0"])
    AssertionManager.assert_list_field_contains(response, "positionList", ["Dev", "Qa"])
    AssertionManager.assert_field_value(response, "layoutSetId", "6703f89e1996ee098")
    AssertionManager.assert_field_value(response, "workingTimeCalendarId", "6703f8ace83cd97ed")
    created_teams.append(response.json())


@pytest.mark.createteam
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_create_team_with_empty_name_returns_400(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_list_team()
    data = create_team_data(name="")
    response = TeamService.create_team(url, data)
    created_teams.append(response.json())
    AssertionManager.assert_status_code_400(response)
    AssertionManager.assert_response_text_empty(response)


@pytest.mark.createteam
def test_create_team_with_name_at_100_char_limit_returns_200(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(
        name="The Visionary Economists: Innovating Sustainable Financial Strategies for a Global Future with Data-")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "name",
                                        "The Visionary Economists: Innovating Sustainable Financial Strategies for a "
                                        "Global Future with Data-")
    created_teams.append(response.json())


@pytest.mark.createteam
def test_create_team_with_name_exceeding_100_char_limit_returns_400():
    url = EndpointTeams.get_base_team()
    data = create_team_data(
        name="The Visionary Economists: Innovating Sustainable Financial Strategies for a Global Future with Data-D")
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.createteam
def test_create_team_with_invalid_characters_in_name_returns_400():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="The<Best=Team>")
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.createteam
def test_create_team_with_valid_roles_ids_array_returns_200(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", roles_ids=["6703f64ba26bb589d", "6703f804da5feb1b0"])
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_list_field_contains(response, "rolesIds", ["6703f64ba26bb589d", "6703f804da5feb1b0"])
    created_teams.append(response.json())


@pytest.mark.createteam
def test_create_team_with_invalid_roles_ids_array_returns_403():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", roles_ids=["invalid", "52bc41359000d"])
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.createteam
def test_create_team_with_valid_position_list_returns_200(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", positions=["Dev", "Qa"])
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_list_field_contains(response, "positionList", ["Dev", "Qa"])
    created_teams.append(response.json())


@pytest.mark.createteam
def test_create_team_with_valid_layout_set_id_returns_200(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", layout_set_id="6703f89e1996ee098")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "layoutSetId", "6703f89e1996ee098")
    created_teams.append(response.json())


@pytest.mark.createteam
def test_create_team_with_invalid_layout_set_id_returns_403():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", layout_set_id="invalid")
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.createteam
def test_create_team_with_valid_working_time_calendar_id_returns_200(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", working_time_calendar_id="6703f8ace83cd97ed")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "workingTimeCalendarId", "6703f8ace83cd97ed")
    created_teams.append(response.json())


@pytest.mark.createteam
def test_create_team_with_invalid_working_time_calendar_id_returns_400():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", working_time_calendar_id="invalid")
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.createteam
def test_create_team_without_optional_fields_returns_200(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "name", "Team Test QA")
    AssertionManager.assert_field_is_null(response, "layoutSetId")
    AssertionManager.assert_field_is_null(response, "workingTimeCalendarId")
    created_teams.append(response.json())


@pytest.mark.createteam
def test_unauthenticated_user_cannot_create_team_returns_401():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data, "invalid_user")
    AssertionManager.assert_status_code_401(response)


@pytest.mark.createteam
def test_user_without_permissions_cannot_create_team_returns_403():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data, "no_team_access_user")
    AssertionManager.assert_status_code_403(response)
