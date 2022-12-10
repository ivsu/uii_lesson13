# базовый образ
FROM python:3.7

# рабочая папка проекта
RUN mkdir -p /home/lesson13
WORKDIR "/home/lesson13"

# установка зависимостей
ADD requirements.txt ./
RUN pip install -r requirements.txt

# установка веб-сервера
#RUN sudo apt install unicorn

# копирование файло проекта; можно сделать сразу из репозитория RUN git clone ...
ADD main.py ./
ADD lesson_env.py ./

RUN mkdir -p lesson_lib
ADD ./lesson_lib/__init__.py ./lesson_lib/
ADD ./lesson_lib/logger.py ./lesson_lib/
ADD ./lesson_lib/predict_number.py ./lesson_lib/
ADD ./lesson_lib/prepare_image.py ./lesson_lib/
# папка для логов
RUN mkdir -p logs
# папка для модели и копирование модели
RUN mkdir -p model
ADD ./model/model_mnist.h5 ./model/

# скрипт запуска
ADD start.sh ./
RUN chmod +x start.sh

# установка net-tools
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    net-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
EXPOSE 8000
#CMD [ "python3.7", "./main.py" ]
#CMD [ "nohup", "uvicorn", "main:app", "--reload",  "--reload-dir", "./lesson_lib/", "--host", "0.0.0.0", "&" ]
CMD [ "uvicorn", "main:app", "--reload",  "--reload-dir", "./lesson_lib/", "--host", "0.0.0.0" ]
#CMD ["/bin/sh", "start.sh"]
#CMD["/bin/bash"]
