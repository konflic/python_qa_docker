# python_qa_docker

## Основные команды

```
docker run [--rm] hello-world - проверка что docker работает
docker run = docker create + docker start [-a] container-id 
docker ps [--all] - посмотреть контейнеры в системе
docker start container-id - запустить остановленный контейнер ()
docker images - посмотреть images в системе
docker system prune - удаляет только контейнеры (-a + images)
docker stop/kill container-id - остановить или убить контейнер
docker build [-t name] dockerfile - создать image из файла dockerfile
```

## Инструкции Dockerfile

```
FROM - базовый образ из которого будет создаваться итоговый
WORKDIR - устанавливает директорию для остальных инструкций
ADD, COPY - команды для копирования и добавления файлов
RUN - выполняет команду в текущем образе и формирует новый 
CMD, ENTRYPOINT - определяют команду при запуске контейнера
ENV - выставляет переменные окружения в контейнере
VOLUME - создать директорию на хосте и установить её в контейнер
EXPOSE - указать контейнеру что этот порт нужно открыть
LABEL - установка лейблов на контейнер
```
