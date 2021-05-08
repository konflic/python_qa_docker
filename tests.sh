#!/bin/bash

# Собираем image с тегом tests
docker build -t tests .

# Запускаем контейнер под именем test_run из image tests
docker run --name test_run tests pytest --browser $1 -n $2

# Копируем из контейнера созданный allure-report
docker cp test_run:/app/allure-report .

# Запускаем хост для отчёта аллюр (утилита лежит локально)
# Хост отчёта нужно будет остановить руками
# Сылка на алюр должна быть своя
~/Downloads/allure/bin/allure serve allure-report

# Удаляем из системы созданный контейнер
docker system prune -f
