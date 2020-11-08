# Устанавливаю базовый образ
FROM python:3.6

# Устанавливаю рабочую директорию внутри контейнера
WORKDIR /app

# Копирую файлы из текущей рабочей папки в текущую рабочую контейнера
COPY . .

# Выполняю необходимые команды
RUN pip install -U pip
RUN pip install -r requirements.txt

# Предустанавливаем команду pytest и отчёт
ENTRYPOINT ["pytest", "--alluredir", "allure-report"]

# Этот параметр можно переопределить при СОЗДАНИИ контейнера т.е. run команде
# Можно исапользовать так `docker run --rm my_tests --browser firefox`
CMD ["--browser", "chrome"]
