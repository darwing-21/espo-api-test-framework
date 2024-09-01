import requests
from core.tools.my_logger import setup_logger

logger = setup_logger('api_manager')


class ApiManager:
    @staticmethod
    def get(url, headers=None, params=None):
        try:
            logger.info(f"GET Request URL: {url} | Params: {params}")
            response = requests.get(url, headers=headers, params=params)
            logger.info(f"Response Status Code: {response.status_code}")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"GET Request failed: {e}")
            raise

    @staticmethod
    def post(url, headers=None, payloads=None, params=None):
        try:
            headers = headers.copy() if headers else {}
            headers.update({'Content-Type': 'application/json'})
            logger.info(f"POST Request URL: {url} | Payload: {payloads} | Params: {params}")
            response = requests.post(url, headers=headers, json=payloads, params=params)
            logger.info(f"Response Status Code: {response.status_code}")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"POST Request failed: {e}")
            raise

    @staticmethod
    def put(url, headers=None, payloads=None, params=None):
        try:
            headers = headers.copy() if headers else {}
            headers.update({'Content-Type': 'application/json'})
            logger.info(f"PUT Request URL: {url} | Payload: {payloads} | Params: {params}")
            response = requests.put(url, headers=headers, json=payloads, params=params)
            logger.info(f"Response Status Code: {response.status_code}")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"PUT Request failed: {e}")
            raise

    @staticmethod
    def delete(url, headers=None, payloads=None, params=None):
        try:
            headers = headers.copy() if headers else {}
            headers.update({'Content-Type': 'application/json'})
            logger.info(f"DELETE Request URL: {url} | Payload: {payloads} | Params: {params}")
            response = requests.delete(url, headers=headers, json=payloads, params=params)
            logger.info(f"Response Status Code: {response.status_code}")
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"DELETE Request failed: {e}")
            raise
