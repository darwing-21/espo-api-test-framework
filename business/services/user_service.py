from core.api.api_request import ApiManager
from core.tools.my_logger import setup_logger
from business.services.authentification import Auth

logger = setup_logger('user_service')


class UserService:
    @staticmethod
    def get_list_user(url, user_type="valid_user"):
        logger.info("Starting the process to get the user list.")
        headers = Auth().build_headers(user_type)
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.get(url, headers=headers)
        logger.info("Finished processing the user list request.")
        return response

    @staticmethod
    def create_user(url, data, user_type="valid_user"):
        logger.info("Starting the process to create a user.")
        headers = Auth().build_headers(user_type, additional_headers={'Content-Type': 'application/json'})
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.post(url, headers=headers, data=data)
        logger.info("Finished processing the create user request.")
        return response

    @staticmethod
    def delete_user(url, user_type="valid_user"):
        logger.info("Starting the process to delete a user.")
        headers = Auth().build_headers(user_type, additional_headers={'Content-Type': 'application/json'})
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.delete(url, headers=headers)
        logger.info("Finished processing the delete user request.")
        return response

    @staticmethod
    def update_user(url, data, user_type="valid_user"):
        logger.info("Starting the process to update a user.")
        headers = Auth().build_headers(user_type, additional_headers={'Content-Type': 'application/json'})
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.put(url, headers=headers, data=data)
        logger.info("Finished processing the update user request.")
        return response

    @staticmethod
    def view_user(url, user_type="valid_user"):
        logger.info("Starting the process to view the user.")
        headers = Auth().build_headers(user_type)
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.get(url, headers=headers)
        logger.info("Finished processing the user view request.")
        return response
