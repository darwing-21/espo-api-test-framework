from faker import Faker
import random
import json

fake = Faker()


def generate_team_data():
    roles_ids = ["66a152cf3fd086e50"]
    layout_set_id = "66b14460b5fe67541"
    working_time_calendar_id = "66b2300c28bb5bbba"
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
