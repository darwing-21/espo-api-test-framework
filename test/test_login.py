import requests
import json


def test_list_team():
    url = "https://espo.spartan-soft.com/api/v1/Team"

    payload = json.dumps({
        "name": "Equipo de ventas",
        "rolesIds": [
            "66a152cf3fd086e50"
        ],
        "positionList": [
            "Gerente"
        ],
        "layoutSetId": "66b14460b5fe67541",
        "workingTimeCalendarId": "66b2300c28bb5bbba"
    })
    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': '23679e40658651eb7f0a075cacc927ee',
        'Espo-Authorization': 'YWRtaW4xOmFkbWluMQ==',
        'Cookie': 'auth-token-secret=5a98ede6a130a63b9dc29491948d26af'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
