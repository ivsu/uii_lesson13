# базовый образ
FROM python:3.7

# клонируем файлы проекта из репозитория
RUN git clone https://git@github.com/ivsu/uii_lesson13 /home/lesson13/
WORKDIR "/home/lesson13/server"

# установка зависимостей
ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# установка net-tools (для отладки)
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
EXPOSE 8000
ENTRYPOINT [ "uvicorn", "main:app", "--reload",  "--reload-dir", "./lesson_lib/", "--host", "0.0.0.0" ]
