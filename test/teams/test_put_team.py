import json
import pytest
from business.endpoints.endpoint_team import EndpointTeams
from business.services.team_service import TeamService
from business.tools.assertion_manager import AssertionManager
from data.team import create_team_data


@pytest.mark.updateteam
def test_update_team_with_min_length_name_returns_200(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(name="T")
    AssertionManager.assert_update_team_schema_file(json.loads(data))
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "name", "T")
    AssertionManager.assert_field_value(response, "id", team1['id'])


@pytest.mark.updateteam
def test_update_team_with_max_length_name_returns_200(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        name="The Visionary Economists: Innovating Sustainable Financial Strategies for a Global Future with Data-")
    AssertionManager.assert_update_team_schema_file(json.loads(data))
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "name",
                                        "The Visionary Economists: Innovating Sustainable Financial Strategies for a "
                                        "Global Future with Data-")
    AssertionManager.assert_field_value(response, "id", team1['id'])


@pytest.mark.updateteam
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_update_team_with_empty_name_returns_400(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        name="")
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateteam
def test_update_team_with_invalid_characters_in_name_returns_400(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(name="The<Best=Team>")
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateteam
def test_update_team_with_name_exceeding_100_characters_returns_400(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        name="The Visionary Economists: Innovating Sustainable Financial Strategies for a Global Future with Data-D")
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateteam
def test_update_team_with_empty_position_list_returns_200(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        positions=[])
    AssertionManager.assert_update_team_schema_file(json.loads(data))
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "id", team1['id'])
    AssertionManager.assert_field_is_empty_list(response, "positionList")


@pytest.mark.updateteam
def test_update_team_with_empty_role_ids_list_returns_200(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        roles_ids=[])
    AssertionManager.assert_update_team_schema_file(json.loads(data))
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "id", team1['id'])
    AssertionManager.assert_field_is_empty_list(response, "rolesIds")


@pytest.mark.updateteam
def test_update_team_with_valid_role_ids_list_returns_200(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        roles_ids=["6703f804da5feb1b0"])
    AssertionManager.assert_update_team_schema_file(json.loads(data))
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "id", team1['id'])
    AssertionManager.assert_list_field_contains(response, "rolesIds", ["6703f804da5feb1b0"])


@pytest.mark.updateteam
def test_update_team_with_non_string_role_ids_returns_400(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        roles_ids=[5252413590852])
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.updateteam
def test_update_team_with_valid_layout_set_id_returns_200(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        layout_set_id="6703f89e1996ee098")
    AssertionManager.assert_update_team_schema_file(json.loads(data))
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "id", team1['id'])
    AssertionManager.assert_field_value(response, "layoutSetId", "6703f89e1996ee098")


@pytest.mark.updateteam
def test_update_team_with_empty_layout_set_id_returns_200(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        layout_set_id="null")
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "id", team1['id'])
    AssertionManager.assert_field_is_null(response, "layoutSetId")


@pytest.mark.updateteam
def test_update_team_with_valid_working_time_calendar_id_returns_200(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        working_time_calendar_id="6703f8ace83cd97ed")
    AssertionManager.assert_update_team_schema_file(json.loads(data))
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "id", team1['id'])
    AssertionManager.assert_field_value(response, "workingTimeCalendarId", "6703f8ace83cd97ed")


@pytest.mark.updateteam
def test_update_team_with_empty_working_time_calendar_id_returns_200(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(
        working_time_calendar_id="null")
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "id", team1['id'])
    AssertionManager.assert_field_is_null(response, "workingTimeCalendarId")


@pytest.mark.updateteam
def test_update_team_with_all_valid_fields_returns_200(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(name="Team Developer", roles_ids=["6703f804da5feb1b0"], positions=["Product Owner", "Backend"],
                            layout_set_id="6703f89e1996ee098", working_time_calendar_id="6703f8ace83cd97ed")
    AssertionManager.assert_update_team_schema_file(json.loads(data))
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "id", team1['id'])
    AssertionManager.assert_field_value(response, "name", "Team Developer")
    AssertionManager.assert_list_field_contains(response, "rolesIds", ["6703f804da5feb1b0"])
    AssertionManager.assert_list_field_contains(response, "positionList", ["Product Owner", "Backend"])
    AssertionManager.assert_field_value(response, "layoutSetId", "6703f89e1996ee098")
    AssertionManager.assert_field_value(response, "workingTimeCalendarId", "6703f8ace83cd97ed")


@pytest.mark.updateteam
def test_update_team_with_non_existent_id_returns_404():
    url = EndpointTeams.get_team_id("invalid")
    data = create_team_data(name="Team Developer")
    response = TeamService.update_team(url, data)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.updateteam
def test_unauthenticated_user_cannot_update_team_returns_401(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(name="Team Developer")
    AssertionManager.assert_update_team_schema_file(json.loads(data))
    response = TeamService.update_team(url, data, "invalid_user")
    AssertionManager.assert_status_code_401(response)


@pytest.mark.updateteam
def test_user_without_permissions_cannot_update_team_returns_403(setup_teardown_team):
    team1 = setup_teardown_team
    url = EndpointTeams.get_team_id(team1['id'])
    data = create_team_data(name="Team Developer")
    AssertionManager.assert_update_team_schema_file(json.loads(data))
    response = TeamService.update_team(url, data, "no_team_access_user")
    AssertionManager.assert_status_code_403(response)
