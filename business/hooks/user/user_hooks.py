from core.tools.my_logger import setup_logger
from business.services.user_service import UserService
from business.endpoints.enpoint_user import EndpointUser

logger = setup_logger('user_hooks')


def before_create_user(data):
    logger.info("Setting up for adding a user.")
    url = EndpointUser().get_base_user()
    response = UserService.create_user(url, data)
    return response


def after_delete_user(id_user):
    logger.info("Setting up for delete a user.")
    url = EndpointUser().get_user_id(id_user)
    response = UserService.delete_user(url)
    return
