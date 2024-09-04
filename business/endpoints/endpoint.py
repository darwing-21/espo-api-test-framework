from enum import Enum
from config.config import BASE_URI


class Endpoint(Enum):
    BASE_TEAM = f"{BASE_URI}/Team"
    BASE_USER = f"{BASE_URI}/User"
