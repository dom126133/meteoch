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

- in order to read easyly the cfg file conbvert it in csv with libreoffice, first in ods in oder to have the possibiliy to choose separator in csv

# Topo

All the calculation are taken from swisstopo https://www.swisstopo.admin.ch/en/transformation-calculation-services or https://www.swisstopo.admin.ch/en/coordinates-conversion-navref

# Unitest

- Install pytest with poetry
- In the test directory enter pytest