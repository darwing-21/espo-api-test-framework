from business.services.team_service import TeamService
from business.endpoints.endpoint_team import EndpointTeams
from business.tools.assertion_manager import AssertionManager


def test_get_default():
    url = EndpointTeams.get_list_team()
    response = TeamService.get_list_team(url, )
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_list_team_schema_file(response)
    AssertionManager.assert_list_not_empty(response)
    AssertionManager.assert_total_greater_than_zero(response)
