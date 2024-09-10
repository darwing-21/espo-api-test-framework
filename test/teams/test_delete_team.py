import pytest
from business.services.team_service import TeamService
from business.endpoints.endpoint_team import EndpointTeams
from business.tools.assertion_manager import AssertionManager


@pytest.mark.deleteteam
def test_delete_team_with_valid_id_returns_200(setup_team):
    team = setup_team
    url = EndpointTeams.get_team_id(team['id'])
    response = TeamService.delete_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_response_is_true(response)


@pytest.mark.deleteteam
def test_delete_team_with_non_existent_id_returns_404():
    url = EndpointTeams.get_team_id("invalid")
    response = TeamService.delete_team(url)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.deleteteam
def test_unauthenticated_user_cannot_delete_team_returns_401(setup_team, teardown_team):
    team = setup_team
    created_teams = teardown_team
    url = EndpointTeams.get_team_id(team['id'])
    response = TeamService.delete_team(url, "invalid_user")
    created_teams.append(team)
    AssertionManager.assert_status_code_401(response)


@pytest.mark.deleteteam
def test_user_without_permissions_cannot_delete_team_returns_403(setup_team, teardown_team):
    team = setup_team
    created_teams = teardown_team
    url = EndpointTeams.get_team_id(team['id'])
    response = TeamService.delete_team(url, "no_team_access_user")
    created_teams.append(team)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.deleteteam
def test_delete_already_deleted_team_returns_404(setup_team):
    team = setup_team
    url = EndpointTeams.get_team_id(team['id'])
    response = TeamService.delete_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_response_is_true(response)
    response2 = TeamService.delete_team(url)
    AssertionManager.assert_status_code_404(response2)
