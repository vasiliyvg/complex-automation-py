# Getting Started
## Preconditions
* Install docker
* Install python3 (e.g.: 3.10.4) and pip
## CLI
Follow next steps:
* Start a web application: `docker compose up the-internet`
* Install dependencies:
  * `pip install -r requirements.txt`
  * `playwright install` # install playwright browsers
* Run all tests: `pytest`
## Docker
Follow next steps:
* Start a web application: `docker compose up the-internet`
* Run tests: `docker compose up automated-testing`