from urllib.parse import urlencode
from business.endpoints.endpoint import Endpoint


class EndpointUser:
    @classmethod
    def get_base_user(cls):
        return Endpoint.BASE_USER.value

    @staticmethod
    def get_default_params():
        return {
            "userType": "internal",
            "select": "isActive,emailAddressIsOptedOut,emailAddressIsInvalid,emailAddress,emailAddressData,"
                      "title,userName,salutationName,firstName,lastName,middleName,name",
            "maxSize": 20,
            "offset": 0,
            "orderBy": "userName",
            "order": "asc"
        }

    @classmethod
    def get_list_user(cls, **kwargs):
        default_params = cls.get_default_params()
        params = {key: kwargs[key] if key in kwargs else default_params[key] for key in default_params}
        params = {k: v for k, v in params.items() if v is not None}
        query_string = urlencode(params)
        return f"{Endpoint.BASE_USER.value}?{query_string}"

    @classmethod
    def get_user_id(cls, id_user):
        return f"{Endpoint.BASE_USER.value}/{id_user}"
