import pytest
from business.hooks.team.setup_teardown import before_create_team, after_delete_team
from business.hooks.user.user_hooks import before_create_user
from data.team import generate_team_data, add_user_team_data
from data.user import generate_user_data


@pytest.fixture(scope="session")
def setup_teardown_team():
    team = before_create_team(generate_team_data())
    yield team.json()
    after_delete_team(team.json()['id'])


@pytest.fixture(scope="session")
def setup_teardown_user():
    user = before_create_user(generate_user_data(teams_id=None))
    yield user.json()
    after_delete_team(user.json()['id'])
