import pytest
from business.endpoints.endpoint_team import EndpointTeams
from business.services.team_service import TeamService
from business.tools.assertion_manager import AssertionManager


@pytest.mark.listuserteam
def test_list_users_of_team_with_valid_id_returns_200(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'])
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_users_schema_file(response)
    AssertionManager.assert_field_value(response, "total", 2)
    AssertionManager.assert_field_value_in_response(response, 'id', "52eb6b7c2a118")


@pytest.mark.listuserteam
def test_list_users_for_non_existent_team_id_returns_404(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team("invalid")
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_404(response)


@pytest.mark.listuserteam
def test_filter_active_users_using_primary_filter_returns_200(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], primaryFilter="active")
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_users_schema_file(response)
    AssertionManager.assert_all_field_values_true(response, "isActive")


@pytest.mark.listuserteam
def test_select_specific_fields_in_response_using_select_parameter_returns_200(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], select="name")
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_users_schema_file(response)
    AssertionManager.assert_field_in_list(response, "name")


@pytest.mark.listuserteam
def test_handle_min_max_size_parameter_returns_200(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], maxSize=1)
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_users_schema_file(response)
    AssertionManager.assert_list_size(response, 1)


@pytest.mark.listuserteam
def test_handle_max_max_size_parameter_returns_200(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], maxSize=1)
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_users_schema_file(response)
    AssertionManager.assert_total_greater_than_zero(response)


@pytest.mark.listuserteam
def test_reject_max_size_above_limit_returns_403(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], maxSize=201)
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_403(response)


@pytest.mark.listuserteam
def test_handle_min_offset_parameter_returns_200(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], offset=0)
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_users_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)


@pytest.mark.listuserteam
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_reject_negative_offset_value_returns_400(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], offset=-1)
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listuserteam
@pytest.mark.xfail(reason="This test case is expected to fail due to known issue.", condition=True)
def test_reject_negative_max_size_value_returns_400(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], maxSize=-1)
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listuserteam
def test_order_results_using_order_by_parameter_returns_200(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], orderBy="name")
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_users_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_ascending(response, "name")


@pytest.mark.listuserteam
def test_reject_invalid_values_in_order_parameter_returns_400(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], orderBy="unknown")
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listuserteam
def test_reject_invalid_order_parameter_returns_400(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], order="unknown")
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_400(response)


@pytest.mark.listuserteam
def test_order_results_ascending_using_order_parameter_returns_200(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], order="asc")
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_ascending(response, "name")


@pytest.mark.listuserteam
def test_order_results_descending_using_order_parameter_returns_200(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'], order="desc")
    response = TeamService.get_list_users_team(url)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_select_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
    AssertionManager.assert_list_order_descending(response, "name")


@pytest.mark.listuserteam
def test_get_users_teams_unauthenticated_user_returns_http_401(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'])
    response = TeamService.get_list_users_team(url, "invalid_user")
    AssertionManager.assert_status_code_401(response)


@pytest.mark.listuserteam
def test_user_without_permissions_cannot_access_users_teams_module_returns_403(setup_teardown_user_team):
    team = setup_teardown_user_team
    url = EndpointTeams.get_list_users_team(team['id'])
    response = TeamService.get_list_users_team(url, "no_team_access_user")
    AssertionManager.assert_status_code_403(response)
