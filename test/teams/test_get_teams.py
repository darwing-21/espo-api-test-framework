import pytest
from business.services.team_service import TeamService
from business.endpoints.endpoint_team import EndpointTeams
from business.tools.assertion_manager import AssertionManager


@pytest.mark.listteam
def test_get_teams_with_valid_field_returns_200(setup_list_team):
    team1 = setup_list_team
    url = EndpointTeams.get_list_team(select="name")
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_field_in_list(response, "name")


@pytest.mark.listteam
def test_get_teams_with_nonexistent_field_ignored_returns_200(setup_list_team):
    team1 = setup_list_team
    url = EndpointTeams.get_list_team(select="unknown")
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_field_in_list(response, "name")
    AssertionManager.assert_field_not_in_list(response, "unknown")


@pytest.mark.listteam
def test_get_teams_with_empty_field_ignored_returns_200(setup_list_team):
    team1 = setup_list_team
    url = EndpointTeams.get_list_team(select="")
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_field_in_list(response, "createdAt")


@pytest.mark.listteam
def test_get_team_with_maxsize_1_returns_200(setup_list_team):
    team1 = setup_list_team
    url = EndpointTeams.get_list_team(maxSize=1)
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_list_size(response, 1)


@pytest.mark.listteam
def test_get_teams_with_maxsize_200_returns_200(setup_list_team):
    team1 = setup_list_team
    url = EndpointTeams.get_list_team(maxSize=200)
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)


@pytest.mark.listteam
def test_get_teams_with_maxsize_exceeding_limit_returns_403(setup_list_team):
    team1 = setup_list_team
    url = EndpointTeams.get_list_team(maxSize=201)
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.listteam
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_get_teams_with_maxsize_below_0_returns_400(setup_list_team):
    team1 = setup_list_team
    url = EndpointTeams.get_list_team(maxSize=-1)
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listteam
def test_get_teams_with_offset_0_returns_200(setup_list_team):
    team1 = setup_list_team
    url = EndpointTeams.get_list_team(offset=0)
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)


@pytest.mark.listteam
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_get_teams_with_negative_offset_returns_400():
    url = EndpointTeams.get_list_team(offset=-1)
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listteam
def test_get_teams_with_valid_orderby_returns_ordered_results_200(setup_list_team):
    team1 = setup_list_team
    url = EndpointTeams.get_list_team(select="", orderBy="layoutSetId")
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_ascending(response, "layoutSetId")


@pytest.mark.listteam
def test_get_teams_with_nonexistent_orderby_returns_400():
    url = EndpointTeams.get_list_team(orderBy="unknown")
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listteam
def test_get_teams_with_empty_orderby_ignored_returns_200(setup_list_team):
    url = EndpointTeams.get_list_team(orderBy="")
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_ascending(response, "name")


@pytest.mark.listteam
def test_get_teams_with_order_asc_returns_ascending_results_200(setup_list_team):
    url = EndpointTeams.get_list_team(order="asc")
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_ascending(response, "name")


@pytest.mark.listteam
def test_get_teams_with_order_desc_returns_descending_results_200(setup_list_team):
    url = EndpointTeams.get_list_team(order="desc")
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_descending(response, "name")


@pytest.mark.listteam
def test_get_teams_with_invalid_order_returns_400():
    url = EndpointTeams.get_list_team(order="unknown")
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listteam
def test_get_teams_with_empty_order_ignored_returns_200(setup_list_team):
    url = EndpointTeams.get_list_team(order="")
    response = TeamService.get_list_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_ascending(response, "name")


@pytest.mark.listteam
def test_get_teams_unauthenticated_user_returns_http_401(setup_list_team):
    url = EndpointTeams.get_list_team()
    response = TeamService.get_list_team(url, "invalid_user")
    AssertionManager.assert_status_code_401(response)


@pytest.mark.listteam1
def test_user_without_permissions_cannot_access_teams_module_returns_403(setup_list_team):
    url = EndpointTeams.get_list_team()
    response = TeamService.get_list_team(url, "no_team_access_user")
    AssertionManager.assert_status_code_403(response)


@pytest.mark.listteam1
def test_get_teams_for_authenticated_user_returns_http_200(setup_list_team):
    url = EndpointTeams.get_list_team()
    response = TeamService.get_list_team(url, "self_teams_user")
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_list_size(response, 1)
