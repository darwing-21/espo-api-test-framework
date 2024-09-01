import requests
from core.tools.my_logger import setup_logger

logger = setup_logger('api_manager')


class ApiManager:

    @staticmethod
    def get(url, headers):
        try:
            logger.info(f"GET Request URL: {url} | {headers}")
            response = requests.get(url, headers=headers)
            logger.info(f"Response Status Code: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"GET Request failed: {e}")
            raise
