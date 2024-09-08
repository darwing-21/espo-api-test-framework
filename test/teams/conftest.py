import pytest
from business.hooks.team.setup_teardown import before_create_team, after_delete_team
from data.team import generate_team_data


@pytest.fixture(scope="module")
def setup_list_team():
    team1 = before_create_team(generate_team_data())
    yield team1.json()
    after_delete_team(team1.json()['id'])


@pytest.fixture(scope="module")
def teardown_team():
    created_teams = []
    yield created_teams
    for team in created_teams:
        after_delete_team(team['id'])


@pytest.fixture(scope="module")
def setup_team():
    team1 = before_create_team(generate_team_data())
    yield team1.json()


@pytest.fixture(scope="function")
def setup_teardown_team():
    team1 = before_create_team(generate_team_data())
    yield team1.json()
    after_delete_team(team1.json()['id'])
