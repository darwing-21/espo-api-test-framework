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
