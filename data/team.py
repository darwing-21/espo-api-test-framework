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
