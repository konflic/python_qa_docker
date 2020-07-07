# Устанавливаю базовый образ
FROM python:3.6
# Устанавливаю рабочую директорию
WORKDIR /app
# Копирую файлы из текущей рабочей папки в текущую рабочую контейнера
COPY . .
# Выполняю необходимые команды
RUN pip install -U pip
RUN pip install -r requirements.txt
# Выполняю запуск тестов
CMD ["pytest", "--alluredir", "allure-report"]
