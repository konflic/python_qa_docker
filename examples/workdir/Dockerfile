FROM ubuntu

RUN mkdir app

# Установка рабочей директории
WORKDIR ./app

COPY ./index.py ./index.py

# Установка рабочей директории в корень
WORKDIR /

CMD ["cat", "app/index.py"]
