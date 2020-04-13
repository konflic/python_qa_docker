#!/bin/bash

docker build -t my_tests .
docker run --name my_run my_tests
docker cp my_run:/app/allure-report .
allure serve allure-report
rm -rf allure-report
docker system prune
