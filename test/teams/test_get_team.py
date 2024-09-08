import pytest
from business.services.team_service import TeamService
from business.endpoints.endpoint_team import EndpointTeams
from business.tools.assertion_manager import AssertionManager


def test_view_team_with_valid_id_returns_200(setup_teardown_team):
    team = setup_teardown_team
    url = EndpointTeams.get_team_id(team['id'])
    response = TeamService.view_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "id", team['id'])


def test_view_team_with_non_existent_id_returns_404():
    url = EndpointTeams.get_team_id("invalid")
    response = TeamService.view_team(url)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_view_deleted_team_returns_404(setup_team):
    team = setup_team
    url = EndpointTeams.get_team_id(team['id'])
    TeamService.delete_team(url)
    response = TeamService.view_team(url)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.lol
def test_unauthenticated_user_cannot_create_team_returns_401(setup_team):
    team = setup_team
    url = EndpointTeams.get_team_id(team['id'])
    response = TeamService.view_team(url, "invalid_user")
    AssertionManager.assert_status_code_401(response)


@pytest.mark.lol
def test_user_without_permissions_cannot_create_team_returns_403(setup_team):
    team = setup_team
    url = EndpointTeams.get_team_id(team['id'])
    response = TeamService.view_team(url, "no_team_access_user")
    AssertionManager.assert_status_code_403(response)
