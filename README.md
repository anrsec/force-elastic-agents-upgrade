# Force Elastic Agents Upgrade

## Description
While upgrading Elastic Agents through Fleet from 8.6.0 to 8.6.1, some agents got stuck in the `UPDATING` state. 

This script will collect information about all agents from Elastic and then will force the upgrade of the agents that are stuck in the `UPDATING` state.

This script uses environment variables for KIBANA_USER, KIBANA_PASSWORD, KIBANA_URL and ELASTIC_VERSION variables.

## Installation
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Usage
Create an `.env` file and add the required variables:  
```
export KIBANA_USER=
export KIBANA_PASSWORD=
export KIBANA_URL=
export ELASTIC_VERSION=
```
Source the `.env` file:  
`source .env`  

Then run the script:  
`python3 force-elastic-agents-upgrade.py`
## Support
[Twitter](https://twitter.com/anrsec)  
[Linkedin](https://www.linkedin.com/in/andrei-rediu/)

## Contributing
Create a pull request or a GitHub issue.

## License
See [here](LICENSE.md).  
In addition to the capabilities listed here, [Bit-Sentinel](https://bit-sentinel.com) maintains several other in-house plugins that offer more advanced automation capabilities. For more information, please reach out to contact@bit-sentinel.com

