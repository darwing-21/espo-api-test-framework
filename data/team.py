from faker import Faker
import random
import json

fake = Faker()


def generate_team_data():
    roles_ids = ["52bd3ee937361", "52bc41359084d"]
    layout_set_id = "66d8f8ff4f1c23bca"
    working_time_calendar_id = "66d8f90b424428d1b"
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
