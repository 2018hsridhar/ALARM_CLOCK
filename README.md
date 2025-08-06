# ALARM_CLOCK
`export PYTHONPATH="/Users/harisrid/Desktop/CODEBASES/ALARM_CLOCK:$PYTHONPATH"`

# My goal : create an application In Python3 to execute 
# PostgreSQL queries and connect to the database


# Docker Components
cd ../yml/docker-compose.yml
docker-compose up -d 

Spins up a PostgresDB on a Docker container
Containerized envs for isolation
Leverage for Enterprise Development and Testing envs

`docker ps | grep -i 'alpine'` - get inside the container
`docker exec -it <docker_id> /bin/bash`
`psql -U harisrid -d harisrid_db`

