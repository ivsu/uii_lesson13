# базовый образ
FROM python:3.7

# установка зависимостей
ADD requirements.txt /
RUN pip install -r  /requirements.txt

ADD main.py /
ENV PYTHONUNBUFFERED=1
CMD [ "python", "./main.py" ]
