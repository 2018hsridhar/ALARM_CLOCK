# INITIALIZATION SCRIPTS
<!-- Activate the virtual env -->
`source /Users/harisrid/Desktop/CODEBASES/ALARM_CLOCK/.venv/bin/activate`
`python3 BACKEND/init.py`
`python3 -m venv .venv`
`source .venv/bin/activate`


# Run alarm clock application
`export PYTHONPATH="/Users/harisrid/Desktop/CODEBASES/ALARM_CLOCK:$PYTHONPATH"`
`python3 APP/app.py`

# Docker Components
# Spins up a PostgresDB on a Docker container
# Containerized envs for isolation
# Leverage for Enterprise Development and Testing envs
cd ../yml/docker-compose.yml
docker-compose up -d 

# Debugging Docker Components
`docker ps | grep -i 'alpine'` - get inside the container
`docker exec -it <docker_id> /bin/bash`
`psql -U harisrid -d harisrid_db`

# Where server listening on 
Bring up ` http://0.0.0.0:5001 ` OR ` http://localhost:5001 `