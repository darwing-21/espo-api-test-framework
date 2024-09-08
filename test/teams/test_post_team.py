import json
import pytest
from business.endpoints.endpoint_team import EndpointTeams
from business.services.team_service import TeamService
from business.tools.assertion_manager import AssertionManager
from data.team import create_team_data


def test_create_team_with_valid_name_returns_201(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", roles_ids=["52bd3ee937361", "52bc41359084d"], positions=["Dev", "Qa"],
                            layout_set_id="66d8f8ff4f1c23bca", working_time_calendar_id="66d8f90b424428d1b")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "name", "Team Test QA")
    AssertionManager.assert_list_field_contains(response, "rolesIds", ["52bd3ee937361", "52bc41359084d"])
    AssertionManager.assert_list_field_contains(response, "positionList", ["Dev", "Qa"])
    AssertionManager.assert_field_value(response, "layoutSetId", "66d8f8ff4f1c23bca")
    AssertionManager.assert_field_value(response, "workingTimeCalendarId", "66d8f90b424428d1b")
    created_teams.append(response.json())


@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_create_team_with_empty_name_returns_400():
    url = EndpointTeams.get_list_team()
    data = create_team_data(name="")
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_400(response)
    AssertionManager.assert_response_text_empty(response)


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


def test_create_team_with_name_exceeding_100_char_limit_returns_400():
    url = EndpointTeams.get_base_team()
    data = create_team_data(
        name="The Visionary Economists: Innovating Sustainable Financial Strategies for a Global Future with Data-D")
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_400(response)


def test_create_team_with_invalid_characters_in_name_returns_400():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="The<Best=Team>")
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_400(response)


def test_create_team_with_valid_roles_ids_array_returns_200(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", roles_ids=["52bd3ee937361", "52bc41359084d"])
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_list_field_contains(response, "rolesIds", ["52bd3ee937361", "52bc41359084d"])
    created_teams.append(response.json())


def test_create_team_with_invalid_roles_ids_array_returns_403():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", roles_ids=["invalid", "52bc41359000d"])
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_403(response)


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


def test_create_team_with_valid_layout_set_id_returns_200(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", layout_set_id="66d8f8ff4f1c23bca")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "layoutSetId", "66d8f8ff4f1c23bca")
    created_teams.append(response.json())


def test_create_team_with_invalid_layout_set_id_returns_403():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", layout_set_id="invalid")
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_403(response)


def test_create_team_with_valid_working_time_calendar_id_returns_200(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", working_time_calendar_id="66d8f90b424428d1b")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "workingTimeCalendarId", "66d8f90b424428d1b")
    created_teams.append(response.json())


def test_create_team_with_invalid_working_time_calendar_id_returns_400():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", working_time_calendar_id="invalid")
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_403(response)


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


def test_unauthenticated_user_cannot_create_team_returns_401():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data, "invalid_user")
    AssertionManager.assert_status_code_401(response)


def test_user_without_permissions_cannot_create_team_returns_403():
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data, "no_team_access_user")
    AssertionManager.assert_status_code_403(response)
