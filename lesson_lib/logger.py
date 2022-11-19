
import os
import logging

# импорт настроек среды проекта
FOLDER_LOGS = os.environ.get('FOLDER_LOGS')
LOG_LEVEL = os.environ.get('LOG_LEVEL')

_log_format = f'%(asctime)s [%(levelname)s] %(name)s %(funcName)s(%(lineno)d): %(message)s'
_log_file = FOLDER_LOGS + 'system.log'

# обработчик для записи лога в файл
def get_file_handler():
    file_handler = logging.FileHandler(_log_file)
    # file_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(LOG_LEVEL)
    
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler

# возвращает инстанс логгера
def get(name):
    logger = logging.getLogger(name)
    # logger.setLevel(logging.DEBUG)
    logger.setLevel(LOG_LEVEL)
    # print(logger.handlers)
    if not logger.handlers:
        logger.addHandler(get_file_handler())

    return logger
