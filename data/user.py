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
        "phoneNumber": "+5917339930",
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


def create_user_data(user_type="regular", is_active=False, user_name=None, salutation_name=None, first_name=None,
                     last_name=None, email_address=None, phone_number=None, gender=None, teams_ids=None,
                     default_team_id=None,
                     roles_ids=None, working_time_calendar_id=None, layout_set_id=None, password=None,
                     avatar_color=None,
                     send_access_info=False):

    salutation_options = ["Mr.", "Mrs.", "Ms.", "Dr."]
    user_data = {
        "type": user_type,
        "isActive": is_active,
        "userName": user_name or fake.user_name(),
        "salutationName": salutation_name or random.choice(salutation_options),
        "firstName": first_name or fake.first_name(),
        "lastName": last_name or fake.last_name(),
        "emailAddress": email_address,
        "phoneNumber": phone_number,
        "gender": gender,
        "teamsIds": teams_ids,
        "defaultTeamId": default_team_id or (random.choice(teams_ids) if teams_ids else None),
        "rolesIds": roles_ids,
        "workingTimeCalendarId": working_time_calendar_id,
        "layoutSetId": layout_set_id,
        "password": password,
        "avatarColor": avatar_color,
        "sendAccessInfo": send_access_info
    }
    user_data = {key: value for key, value in user_data.items() if value is not None}
    user_data = {key: (None if value == "null" else value) for key, value in user_data.items()}

    return json.dumps(user_data)
