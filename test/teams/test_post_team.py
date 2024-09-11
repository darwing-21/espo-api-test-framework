import json
import pytest
from business.endpoints.endpoint_team import EndpointTeams
from business.services.team_service import TeamService
from business.tools.assertion_manager import AssertionManager
from data.team import create_team_data


@pytest.mark.createteam
def test_create_team_with_valid_name_returns_201(teardown_team):
    created_teams = teardown_team
    url = EndpointTeams.get_base_team()
    data = create_team_data(name="Team Test QA", roles_ids=["52bd3ee937361", "52bc41359084d"], positions=["Dev", "Qa"],
                            layout_set_id="66d8f8ff4f1c23bca", working_time_calendar_id="66d8f90b424428d1b")
    AssertionManager.assert_create_team_schema_file(json.loads(data))
    response = TeamService.create_team(url, data)
    AssertionManager.assert_status_code_200(response)
    AssertionManager.assert_team_general_schema_file(response)
    AssertionManager.assert_field_value(response, "name", "Team Test QA")
    AssertionManager.assert_list_field_contains(response, "rolesIds", ["52bd3ee937361", "52bc41359084d"])
    AssertionManager.assert_list_field_contains(response, "positionList", ["Dev", "Qa"])
    AssertionManager.assert_field_value(response, "layoutSetId", "66d8f8ff4f1c23bca")
    AssertionManager.assert_field_value(response, "workingTimeCalendarId", "66d8f90b424428d1b")
    created_teams.append(response.json())


