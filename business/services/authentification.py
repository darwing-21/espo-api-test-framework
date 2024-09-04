from core.tools.load_file_json import load_credential_config
from core.api.auth_manager import get_headers
from core.tools.my_logger import setup_logger

logger = setup_logger('auth_service')


class Auth:
    def __init__(self):
        logger.info("Initializing Auth class.")
        self.users = self.load_file()
        self.header_builder = get_headers()
        logger.info("Auth class initialized successfully.")

    @staticmethod
    def load_file():
        logger.info("Loading credential configuration from 'credentials.json'.")
        try:
            return load_credential_config("credentials.json")
        except FileNotFoundError as e:
            logger.error("Credentials file not found: 'credentials.json'", exc_info=True)
            raise
        except Exception as e:
            logger.error("An error occurred while loading credentials.", exc_info=True)
            raise

    def get_user(self, user_type):
        logger.info(f"Fetching user details for user type: '{user_type}'")
        user = self.users.get(user_type)
        if not user:
            logger.warning(f"User type '{user_type}' not found in credentials.")
        else:
            logger.debug(f"User details found: {user}")
        return user

    def build_headers(self, user_type):
        logger.info(f"Building headers for user type: '{user_type}'")
        user = self.get_user(user_type)
        if not user:
            logger.error(f"User type '{user_type}' not found in credentials.")
            raise ValueError(f"User type '{user_type}' not found in credentials.")

        username = user.get("username")
        password = user.get("password")

        headers = self.header_builder(username, password)
        logger.info(f"Headers successfully built for user type: '{user_type}'")
        logger.debug(f"Headers: {headers}")
        return headers
