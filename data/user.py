from faker import Faker
import random
import json

fake = Faker()


def generate_user_data(teams_id):
    teams_ids = teams_id
    roles_ids = ["52bd3ee937361", "52bc41359084d"]
    layout_set_id = "66d8f8ff4f1c23bca"
    working_time_calendar_id = "66d8f90b424428d1b"
    avatar_color = "#ef2b2b"
    salutation_options = ["Mr.", "Mrs.", "Ms.", "Dr."]

    user_data = {
        "type": "regular",
        "isActive": True,
        "userName": fake.user_name(),
        "salutationName": random.choice(salutation_options),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "title": fake.job(),
        "emailAddress": fake.email(),
        "phoneNumber": "+5917229930",
        "gender": random.choice(["Male", "Female", "Neutral"]),
        "teamsIds": teams_ids,
        "defaultTeamId": random.choice(teams_ids),
        "rolesIds": roles_ids,
        "workingTimeCalendarId": working_time_calendar_id,
        "layoutSetId": layout_set_id,
        "password": fake.password(length=8),
        "avatarColor": avatar_color,
        "sendAccessInfo": False
    }
    return json.dumps(user_data)
