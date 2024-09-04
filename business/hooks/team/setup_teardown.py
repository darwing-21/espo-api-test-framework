from core.tools.my_logger import setup_logger
from business.services.team_service import TeamService
from business.endpoints.endpoint_team import EndpointTeams

logger = setup_logger('team_hooks')


def before_create_team(data):
    logger.info("Setting up for adding a team.")
    url = EndpointTeams().get_base_team()
    response = TeamService.create_team(url, data)
    return response


def after_delete_team(id_team):
    logger.info("Setting up for delete a team.")
    url = EndpointTeams().get_team_id(id_team)
    response = TeamService.delete_team(url)
    return response
