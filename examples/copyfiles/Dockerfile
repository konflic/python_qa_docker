FROM ubuntu:18.04

# Сатвим питон
RUN apt update -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update -y
RUN apt install python3.6 -y

# Копируем файлы
ADD ./index.py ./index.py

# Команда по умолчанию, можно переопределить
CMD ["python3", "index.py"]
