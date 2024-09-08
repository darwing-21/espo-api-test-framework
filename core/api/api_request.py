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

    @staticmethod
    def post(url, headers, data):
        try:
            logger.info(f"POST Request URL: {url} | {headers}")
            response = requests.post(url, headers=headers, data=data)
            logger.info(f"Response Status Code: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"POST Request failed: {e}")
            raise

    @staticmethod
    def put(url, headers, data):
        try:
            logger.info(f"PUT Request URL: {url} | {headers}")
            response = requests.put(url, headers=headers, data=data)
            logger.info(f"Response Status Code: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"PUT Request failed: {e}")
            raise

    @staticmethod
    def delete(url, headers, data=None):
        try:
            logger.info(f"DELETE Request URL: {url} | {headers}")
            response = requests.delete(url, headers=headers, data=data)
            logger.info(f"Response Status Code: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"DELETE Request failed: {e}")
            raise
