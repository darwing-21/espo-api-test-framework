from faker import Faker
import random
import json

fake = Faker()


def generate_team_data():
    roles_ids = ["6703f64ba26bb589d", "6703f804da5feb1b0"]
    layout_set_id = "6703f89e1996ee098"
    working_time_calendar_id = "6703f8ace83cd97ed"
    team_name = f"Team test {fake.word()}"
    positions = random.sample(["Scrum Master", "Dev", "Qa", "Designer", "Product Owner"],
                              k=3)
    team_data = {
        "name": team_name,
        "rolesIds": roles_ids,
        "positionList": positions,
        "layoutSetId": layout_set_id,
        "workingTimeCalendarId": working_time_calendar_id
    }

    return json.dumps(team_data)


def create_team_data(roles_ids=None, layout_set_id=None, working_time_calendar_id=None,
                     name=None, positions=None):
    team_data = {
        "name": name,
        "rolesIds": roles_ids,
        "positionList": positions,
        "layoutSetId": layout_set_id,
        "workingTimeCalendarId": working_time_calendar_id
    }
    team_data = {key: value for key, value in team_data.items() if value is not None}
    team_data = {key: (None if value == "null" else value) for key, value in team_data.items()}
    return json.dumps(team_data)


def add_user_team_data(users_ids=None):
    users_id_data = {
        "ids": users_ids
    }
    return json.dumps(users_id_data)


def delete_user_team_data(user_id):
    user_id_data = {
        "id": user_id
    }
    return json.dumps(user_id_data)
