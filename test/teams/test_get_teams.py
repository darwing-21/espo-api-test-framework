from business.services.team_service import TeamService
from business.endpoints.endpoint_team import EndpointTeams


def test_get_default():
    url = EndpointTeams.get_list_team()
    response = TeamService.get_list_team(url)
