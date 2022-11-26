# базовый образ
FROM python:3.7

# установка зависимостей
ADD requirements.txt /lesson13
RUN pip install -r  /lesson13/requirements.txt

ADD main.py /lesson13/
ADD lesson_env.py /lesson13/

RUN mkdir -p lesson_lib
ADD ./lesson_lib/__init__.py /lesson13/lesson_lib/
ADD ./lesson_lib/logger.py /lesson13/lesson_lib/
ADD ./lesson_lib/predict_number.py /lesson13/lesson_lib/
ADD ./lesson_lib/prepare_image.py /lesson13/lesson_lib/

RUN mkdir -p logs

RUN mkdir -p model
ADD ./model/model_mnist.h5 /lesson13/model/

WORKDIR /lesson13/

ENV PYTHONUNBUFFERED=1
CMD [ "python3.7", "./main.py" ]
