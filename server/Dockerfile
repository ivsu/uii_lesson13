# базовый образ
FROM python:3.7

# клонируем файлы проекта из репозитория
RUN git clone https://git@github.com/ivsu/uii_lesson13 /home/lesson13/
WORKDIR "/home/lesson13/server"

# рабочая папка проекта
# RUN mkdir -p /home/lesson13
# WORKDIR "/home/lesson13"
# копирование файло проекта; можно сделать сразу из репозитория RUN git clone ...

# ADD *.py ./
# ADD lesson_env.py .
# модули проекта
# RUN mkdir lesson_lib
# ADD ./lesson_lib/ ./lesson_lib/
# папка для модели и копирование модели
# RUN mkdir model
# ADD ./model/model_mnist.h5 ./model/
# папка для логов
# RUN mkdir logs

# установка зависимостей
ADD requirements.txt ./
RUN pip install -r requirements.txt

# установка net-tools
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    net-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
EXPOSE 8000
ENTRYPOINT [ "uvicorn", "main:app", "--reload",  "--reload-dir", "./lesson_lib/", "--host", "0.0.0.0" ]
