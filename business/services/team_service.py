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
