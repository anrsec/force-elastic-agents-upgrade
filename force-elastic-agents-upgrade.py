import requests
import json
import os

# Get the enviroment variables
KIBANA_USER = os.environ['KIBANA_USER']
KIBANA_PASSWORD = os.environ['KIBANA_PASSWORD']
ELASTIC_VERSION = os.environ['ELASTIC_VERSION']

# Get a list of agent with name, id and status
def get_agents():
    KIBANA_URL = os.environ['KIBANA_URL'] + 'api/fleet/agents?perPage=1000'
    response = requests.get(KIBANA_URL, auth=(KIBANA_USER, KIBANA_PASSWORD))
    response_json = json.loads(response.text)
    agents = []
    for agent in response_json["list"]:
        agents.append({
            "agent_name" : agent["local_metadata"]["host"]["hostname"],
            "agent_status" : agent["status"],
            "agent_id" : agent["id"]
        })
    return agents

# Function to force an upgrade of an Elastic Agent
def force_agent_upgrade(agent_id):
    KIBANA_URL = os.environ['KIBANA_URL'] + 'api/fleet/agents/' + agent_id + '/upgrade'
    response = requests.post(KIBANA_URL, auth=(KIBANA_USER, KIBANA_PASSWORD), data={
    "version": ELASTIC_VERSION,
	"force": "true"
    }, headers={
    "kbn-xsrf": "as"
    } )
    return response

# Get the agents
agents = get_agents()

# Initialize the list of upgraded agents
upgraded_agents = []

# Loop through the agents and force an upgrade if the status is updating
for agent in agents:
    if agent["agent_status"] == "updating" and agent["agent_name"] != "unm-srv-app0":
        upgrade_response = force_agent_upgrade(agent["agent_id"])
        if upgrade_response.status_code == 200:
            upgraded_agents.append(agent["agent_name"])

# Print the list of upgraded agents
print(f"Upgraded agents:\n{ upgraded_agents }")