import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(name, log_file='logs/combined.log', level=logging.INFO):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(name)
    if not logger.handlers:
        file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    logger.setLevel(level)

    return logger


if __name__ == "__main__":
    logger = setup_logger('espo_API')
    logger.info("Logger is configured and ready to use!")
