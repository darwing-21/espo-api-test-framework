import base64
from core.tools.my_logger import setup_logger
from config.config import X_Api_Key

logger = setup_logger('auth_manager')


def encoded(username: str, password: str) -> str:
    logger.info(f"Encoding credentials for user: {username}")
    credentials = f'{username}:{password}'
    encode = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    logger.debug(f"Encoded credentials: {encode}")
    return encode


def get_headers():
    def _get_headers(username: str, password: str, additional_params: dict = None) -> dict:
        logger.info(f"Building headers for user: {username}")
        espo_authorization = encoded(username, password)
        headers = {
            'Espo-Authorization': espo_authorization,
            'X-Api-Key': X_Api_Key
        }
        if additional_params:
            logger.debug(f"Adding additional parameters to headers: {additional_params}")
            headers.update(additional_params)

        logger.info(f"Headers build successfully for user: {username}")
        logger.debug(f"Headers: {headers}")
        return headers

    return _get_headers
