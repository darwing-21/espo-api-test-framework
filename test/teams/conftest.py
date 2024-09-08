import pytest
from business.hooks.team.setup_teardown import before_create_team, after_delete_team, before_add_user
from data.team import generate_team_data, add_user_team_data


@pytest.fixture(scope="module")
def setup_list_team():
    team1 = before_create_team(generate_team_data())
    yield team1.json()
    after_delete_team(team1.json()['id'])


@pytest.fixture(scope="function")
def teardown_team():
    created_teams = []
    yield created_teams
    for team in created_teams:
        after_delete_team(team['id'])


@pytest.fixture(scope="function")
def setup_team():
    team1 = before_create_team(generate_team_data())
    yield team1.json()


@pytest.fixture(scope="function")
def setup_teardown_team():
    team1 = before_create_team(generate_team_data())
    yield team1.json()
    after_delete_team(team1.json()['id'])


@pytest.fixture(scope="module")
def setup_teardown_user_team():
    team1 = before_create_team(generate_team_data())
    users_ids = add_user_team_data(["52eb6b7c2a118", "53203b9428742"])
    before_add_user(team1.json()['id'], users_ids)
    yield team1.json()
    after_delete_team(team1.json()['id'])
