from urllib.parse import urlencode

from bussines.endpoints.endpoint import Endpoint


class EndpointTeams:
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
