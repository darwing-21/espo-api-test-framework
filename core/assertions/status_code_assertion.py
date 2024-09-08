from core.tools.my_logger import setup_logger

logger = setup_logger('status_code_assertion')


class StatusCodeAssertion:
    @staticmethod
    def assert_status_code_200(response):
        logger.info(f"Validating status code 200 for response with URL: {response.url}")
        try:
            assert response.status_code == 200, (
                f"Expected status code 200, but got {response.status_code}. Response text: {response.text}"
            )
            logger.info("Status code 200 validated successfully.")
            assert response.text, "Expected non-empty response body, but got an empty response."
            logger.info("Response body is not empty.")
        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            raise

    @staticmethod
    def assert_status_code_403(response):
        logger.info(f"Validating status code 403 for response with URL: {response.url}")
        try:
            assert response.status_code == 403, (
                f"Expected status code 403, but got {response.status_code}. Response text: {response.text}"
            )
            logger.info("Status code 403 validated successfully.")
        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            raise

    @staticmethod
    def assert_status_code_400(response):
        logger.info(f"Validating status code 400 for response with URL: {response.url}")
        try:
            assert response.status_code == 400, (
                f"Expected status code 400, but got {response.status_code}. Response text: {response.text}"
            )
            logger.info("Status code 400 validated successfully.")
        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            raise

    @staticmethod
    def assert_status_code_401(response):
        logger.info(f"Validating status code 401 for response with URL: {response.url}")
        try:
            assert response.status_code == 401, (
                f"Expected status code 401, but got {response.status_code}. Response text: {response.text}"
            )
            logger.info("Status code 401 validated successfully.")
        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            raise

    @staticmethod
    def assert_status_code_404(response):
        logger.info(f"Validating status code 404 for response with URL: {response.url}")
        try:
            assert response.status_code == 404, (
                f"Expected status code 404, but got {response.status_code}. Response text: {response.text}"
            )
            logger.info("Status code 404 validated successfully.")
        except AssertionError as e:
            logger.error(f"Assertion failed: {e}")
            raise
