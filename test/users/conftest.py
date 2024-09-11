import pytest
from business.hooks.user.user_hooks import before_create_user, after_delete_user
from data.user import generate_user_data


@pytest.fixture(scope="module")
def setup_teardown_user(setup_teardown_team_global):
    team = setup_teardown_team_global
    user = before_create_user(generate_user_data([team['id']]))
    yield user.json()
    after_delete_user(user.json()['id'])


@pytest.fixture(scope="function")
def teardown_user():
    created_user = []
    yield created_user
    for user in created_user:
        after_delete_user(user['id'])


@pytest.fixture(scope="function")
def setup_teardown_user_function(setup_teardown_team_global):
    team = setup_teardown_team_global
    user = before_create_user(generate_user_data([team['id']]))
    yield user.json()
    after_delete_user(user.json()['id'])


@pytest.fixture(scope="function")
def setup_user(setup_teardown_team_global):
    team = setup_teardown_team_global
    user = before_create_user(generate_user_data([team['id']]))
    yield user.json()
