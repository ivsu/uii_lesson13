import os

# настройки проекта

# f = open("/content/lesson13/debug.txt", "w")
# f.write(__name__)
# f.close()

# структура папок
# FOLDER_LIB = './lesson_lib/'
# FOLDER_MODEL = './model/'
# FOLDER_LOGS = './logs/'
os.environ['FOLDER_APP'] = './app/'
os.environ['FOLDER_MODEL'] = './model/'
os.environ['FOLDER_LOGS'] = './logs/'

# файл модели
# MODEL_FILE = 'model_mnist.h5'
os.environ['MODEL_FILE'] = 'model_mnist.h5'

# уровень логгирования
# LOG_LEVEL = 'DEBUG'
os.environ['LOG_LEVEL'] = 'DEBUG'

print('env executed')
