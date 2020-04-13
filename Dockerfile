FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD ["pytest", "--alluredir", "allure-report"]
