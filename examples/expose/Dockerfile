FROM python:alpine

LABEL version="1.0"

COPY ./index.html ./index.html

# Дали возможность добраться до порта
# docker run -p 80:8000
EXPOSE 8000

# Ещё один способ записать команду
CMD python3 -m http.server
