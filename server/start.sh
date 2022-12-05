#!/bin/sh
# запуск веб-сервера
nohup uvicorn main:app --reload --reload-dir ./lesson_lib/ &
