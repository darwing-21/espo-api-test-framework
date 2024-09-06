import pytest
from business.hooks.team.setup_teardown import before_create_team, after_delete_team
from data.team import generate_team_data


@pytest.fixture(scope="module")
def setup_list_team():
    team1 = before_create_team(generate_team_data())
    # team2 = before_create_team(generate_team_data())
    # team3 = before_create_team(generate_team_data())
    yield team1.json()
    after_delete_team(team1.json()['id'])
    # after_delete_team(team2.json()['id'])
    # after_delete_team(team3.json()['id'])
