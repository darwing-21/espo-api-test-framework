import json
import pytest
from business.endpoints.endpoint_team import EndpointTeams
from business.services.team_service import TeamService
from business.tools.assertion_manager import AssertionManager
from data.team import add_user_team_data


def test_link_valid_user_to_team_with_valid_id_returns_200(setup_teardown_team):
    team = setup_teardown_team
    url = EndpointTeams.get_team_user(team['id'])
    data = add_user_team_data([])