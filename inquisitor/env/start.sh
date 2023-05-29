docker-compose up -d
docker network inspect env_inquisitor_network | grep -e IPv4 -e Name -e Mac
