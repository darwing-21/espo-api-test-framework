from urllib.parse import urlencode
from business.endpoints.endpoint import Endpoint


class EndpointTeams:
    @classmethod
    def get_base_team(cls):
        return Endpoint.BASE_TEAM.value

    @staticmethod
    def get_default_params():
        return {
            "select": "name",
            "maxSize": 20,
            "offset": 0,
            "orderBy": "name",
            "order": "asc"
        }

    @classmethod
    def get_list_team(cls, **kwargs):
        default_params = cls.get_default_params()
        params = {key: kwargs[key] if key in kwargs else default_params[key] for key in default_params}
        params = {k: v for k, v in params.items() if v is not None}
        query_string = urlencode(params)
        return f"{Endpoint.BASE_TEAM.value}?{query_string}"

    @classmethod
    def get_team_id(cls, id_team):
        return f"{Endpoint.BASE_TEAM.value}/{id_team}"

    @classmethod
    def get_team_user(cls, id_team):
        return f"{Endpoint.BASE_TEAM.value}/{id_team}/users"

    @staticmethod
    def get_default_user_params():
        return {
            "primaryFilter": "active",
            "select": "teamRole,userName,salutationName,firstName,lastName,middleName,name",
            "maxSize": 5,
            "offset": 0,
            "orderBy": "userName",
            "order": "asc"
        }

    @classmethod
    def get_team_users(cls, team_id, **kwargs):
        default_params = cls.get_default_user_params()
        params = {key: kwargs.get(key, default_params[key]) for key in default_params}
        params = {k: v for k, v in params.items() if v is not None}
        query_string = urlencode(params)
        return f"{Endpoint.BASE_TEAM.value}/{team_id}/users?{query_string}"
