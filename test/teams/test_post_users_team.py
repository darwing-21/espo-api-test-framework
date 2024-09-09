import json
import pytest
from business.endpoints.endpoint_team import EndpointTeams
from business.services.team_service import TeamService
from business.tools.assertion_manager import AssertionManager
from data.team import add_user_team_data


@pytest.mark.adduserteam
def test_link_valid_user_to_team_with_valid_id_returns_200(setup_teardown_team):
    team = setup_teardown_team
    url = EndpointTeams.get_team_user(team['id'])
    data = add_user_team_data(["52eb6b7c2a118"])
    AssertionManager.assert_add_users_to_team_schema_file(json.loads(data))
    response = TeamService.add_users_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_response_is_true(response)
    team_user = TeamService.get_list_users_team(url)
    AssertionManager.assert_field_value_in_response(team_user, "id", "52eb6b7c2a118")


@pytest.mark.adduserteam
def test_link_multiple_valid_users_to_team_with_valid_id_returns_200(setup_teardown_team):
    team = setup_teardown_team
    url = EndpointTeams.get_team_user(team['id'])
    data = add_user_team_data(["52eb6b7c2a118", "53203b9428742"])
    AssertionManager.assert_add_users_to_team_schema_file(json.loads(data))
    response = TeamService.add_users_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_response_is_true(response)
    team_user = TeamService.get_list_users_team(url)
    AssertionManager.assert_field_value_in_response(team_user, "id", "52eb6b7c2a118")
    AssertionManager.assert_field_value_in_response(team_user, "id", "53203b9428742")


@pytest.mark.adduserteam
def test_link_users_to_team_with_non_existent_id_returns_404(setup_teardown_team):
    team = setup_teardown_team
    url = EndpointTeams.get_team_user('invalid')
    data = add_user_team_data(["52eb6b7c2a118", "53203b9428742"])
    AssertionManager.assert_add_users_to_team_schema_file(json.loads(data))
    response = TeamService.add_users_team(url, data)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.adduserteam
def test_link_empty_user_id_array_to_team_returns_200(setup_teardown_team):
    team = setup_teardown_team
    url = EndpointTeams.get_team_user(team['id'])
    data = add_user_team_data(users_ids=None)
    response = TeamService.add_users_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_response_is_false(response)


@pytest.mark.adduserteam
def test_link_user_with_invalid_or_non_existent_id_returns_404(setup_teardown_team):
    team = setup_teardown_team
    url = EndpointTeams.get_team_user(team['id'])
    data = add_user_team_data(["invalid"])
    response = TeamService.add_users_team(url, data)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.adduserteam
def test_link_user_teams_unauthenticated_user_returns_http_401(setup_teardown_team):
    team = setup_teardown_team
    url = EndpointTeams.get_team_user(team['id'])
    data = add_user_team_data(["52eb6b7c2a118", "53203b9428742"])
    AssertionManager.assert_add_users_to_team_schema_file(json.loads(data))
    response = TeamService.add_users_team(url, data, "invalid_user")
    AssertionManager.assert_status_code_401(response)


@pytest.mark.adduserteam
def test_user_without_permissions_cannot_access_link_user_teams_module_returns_403(setup_teardown_team):
    team = setup_teardown_team
    url = EndpointTeams.get_team_user(team['id'])
    data = add_user_team_data(["52eb6b7c2a118", "53203b9428742"])
    AssertionManager.assert_add_users_to_team_schema_file(json.loads(data))
    response = TeamService.add_users_team(url, data, "no_team_access_user")
    AssertionManager.assert_status_code_403(response)
