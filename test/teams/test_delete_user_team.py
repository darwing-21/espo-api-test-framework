import json
import pytest
from business.endpoints.endpoint_team import EndpointTeams
from business.services.team_service import TeamService
from business.tools.assertion_manager import AssertionManager
from data.team import delete_user_team_data


@pytest.mark.removeuserteam
def test_unlink_valid_user_from_team_with_valid_id_returns_200(setup_teardown_user_team_function):
    team = setup_teardown_user_team_function
    url = EndpointTeams.get_team_user(team['id'])
    data = delete_user_team_data("53203b9428742")
    AssertionManager.assert_remove_user_from_team_schema_file(json.loads(data))
    response = TeamService.remove_user_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_response_is_true(response)
    team_user = TeamService.get_list_users_team(url)
    AssertionManager.assert_field_value_not_in_response(team_user, "id", "53203b9428742")


@pytest.mark.removeuserteam
def test_unlink_user_from_non_existent_team_id_returns_404(setup_teardown_user_team_function):
    team = setup_teardown_user_team_function
    url = EndpointTeams.get_team_user("invalid")
    data = delete_user_team_data("53203b9428742")
    AssertionManager.assert_remove_user_from_team_schema_file(json.loads(data))
    response = TeamService.remove_user_team(url, data)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.removeuserteam
def test_unlink_user_with_empty_id_returns_200(setup_teardown_user_team_function):
    team = setup_teardown_user_team_function
    url = EndpointTeams.get_team_user(team['id'])
    data = delete_user_team_data(user_id=None)
    response = TeamService.remove_user_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_response_is_false(response)


@pytest.mark.removeuserteam
def test_unlink_user_with_non_existent_id_returns_404(setup_teardown_user_team_function):
    team = setup_teardown_user_team_function
    url = EndpointTeams.get_team_user(team['id'])
    data = delete_user_team_data("invalid")
    response = TeamService.remove_user_team(url, data)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.removeuserteam
def test_unlink_user_teams_unauthenticated_user_returns_http_401(setup_teardown_user_team_function):
    team = setup_teardown_user_team_function
    url = EndpointTeams.get_team_user(team['id'])
    data = delete_user_team_data("53203b9428742")
    AssertionManager.assert_remove_user_from_team_schema_file(json.loads(data))
    response = TeamService.remove_user_team(url, data, "invalid_user")
    AssertionManager.assert_status_code_401(response)


@pytest.mark.removeuserteam
def test_user_without_permissions_cannot_access_unlink_user_teams_module_returns_403(setup_teardown_user_team_function):
    team = setup_teardown_user_team_function
    url = EndpointTeams.get_team_user(team['id'])
    data = delete_user_team_data("53203b9428742")
    AssertionManager.assert_remove_user_from_team_schema_file(json.loads(data))
    response = TeamService.remove_user_team(url, data, "no_team_access_user")
    AssertionManager.assert_status_code_403(response)
