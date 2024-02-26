# make requirements.txt from poetry

poetry export -f requirements.txt --output requirements.txt

# Docker image

## create image and push image to dockerhub

docker build -t bigmil/meteoch:latest .
docker push bigmil/meteoch

## docker misc.

docker image ls
docker tag meteoch bigmil/meteoch

# MosMix

- https://www.dwd.de/EN/ourservices/met_application_mosmix/met_application_mosmix.html
