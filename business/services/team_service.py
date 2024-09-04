from core.api.api_request import ApiManager
from core.tools.my_logger import setup_logger
from business.services.authentification import Auth

logger = setup_logger('team_service')


class TeamService:
    @staticmethod
    def get_list_team(url, user_type="valid_user"):
        logger.info("Starting the process to get the team list.")
        headers = Auth().build_headers(user_type)
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.get(url, headers=headers)
        logger.info("Finished processing the team list request.")
        return response

    @staticmethod
    def create_team(url, data, user_type="valid_user"):
        logger.info("Starting the process to create a team.")
        headers = Auth().build_headers(user_type, additional_headers={'Content-Type': 'application/json'})
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.post(url, headers=headers, data=data)
        logger.info("Finished processing the create team request.")
        return response

    @staticmethod
    def delete_team(url, user_type="valid_user"):
        logger.info("Starting the process to delete a team.")
        headers = Auth().build_headers(user_type, additional_headers={'Content-Type': 'application/json'})
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.delete(url, headers=headers)
        logger.info("Finished processing the delete team request.")
        return response

    @staticmethod
    def update_team(url, data, user_type="valid_user"):
        logger.info("Starting the process to update a team.")
        headers = Auth().build_headers(user_type, additional_headers={'Content-Type': 'application/json'})
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.put(url, headers=headers, data=data)
        logger.info("Finished processing the update team request.")
        return response

    @staticmethod
    def view_team(url, user_type="valid_user"):
        logger.info("Starting the process to view the team.")
        headers = Auth().build_headers(user_type)
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.get(url, headers=headers)
        logger.info("Finished processing the team view request.")
        return response

    @staticmethod
    def view_users_team(url, user_type="valid_user"):
        logger.info("Starting the process to get the users of the team.")
        headers = Auth().build_headers(user_type)
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.get(url, headers=headers)
        logger.info("Finished processing the users team list request.")
        return response

    @staticmethod
    def add_users_team(url, data, user_type="valid_user"):
        logger.info("Starting the process to add users to the team.")
        headers = Auth().build_headers(user_type, additional_headers={'Content-Type': 'application/json'})
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.post(url, headers=headers, data=data)
        logger.info("Finished processing the add users to team request.")
        return response

    @staticmethod
    def remove_user_team(url, user_type="valid_user"):
        logger.info("Starting the process to remove a user from the team.")
        headers = Auth().build_headers(user_type, additional_headers={'Content-Type': 'application/json'})
        logger.debug(f"Preparing headers for the request: {headers}")
        response = ApiManager.delete(url, headers=headers)
        logger.info("Finished processing the remove user from team request.")
        return response
