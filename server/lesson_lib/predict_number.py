# импорт файлов проекта
from . import logger
from .prepare_image import prepare_image

# загрузка стандартных библиотек
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import array_to_img
from io import BytesIO
from PIL import Image 
import sys, os

# инициализация модели
# MODEL_PATH = env.FOLDER_MODEL + env.MODEL_FILE
MODEL_PATH = os.environ.get('FOLDER_MODEL') + os.environ.get('MODEL_FILE')
model = load_model(MODEL_PATH)

log = logger.get(__name__)

def predict_number(image_file):

    # откроем файл
    img_src = Image.open(BytesIO(image_file), mode='r')
    log.debug('Открыт файл изображения')

    try:
        imgs = []
        result = []
        # будем использовать различный порог удаления шумов с изображения
        for lum_threshold in [128, 160, 192, 224, 232, 240, 248]:
            # получим значимую часть изображения
            log.debug(f'Перед обработкой изображения для lum {lum_threshold}')
            img = prepare_image(img_src, size=28, lum_threshold=lum_threshold, verbose=0) #, trace=trace)
            log.debug(f'Изображение получено для lum {lum_threshold}')
            imgs.append(img)
            log.debug(f'Обработано изображение для lum {lum_threshold}')
            # сделаем плоский вектор для dense-модели и нормализуем изображение
            conv_img = imgs[-1].reshape((1, -1)) / 255.
            # выполним предсказание
            pred = model.predict(conv_img)
            log.debug(f'Предсказание выполнено для lum {lum_threshold}')
            # получим индекс наиболее вероятного предсказания
            i = np.argmax(pred[0])
            # запомним результат предсказания при текущем пороге удаления шумов
            result.append([i, pred[0, i]])

        # получим индекс лучшего предсказания по разным порогам удаления шумов
        best = np.argmax(np.array(result)[:, 1])

    except Exception as e:
        return {'error': str(e)}

    log.debug(f'Перед конвертацией в Image')
    img = array_to_img(np.expand_dims(imgs[best], axis=-1))
    img = img.convert('RGB')

    # сериализуем изображение
    img_bytes = BytesIO()
    log.debug(f'Перед сохранением в BytesIO')
    img.save(img_bytes, format='JPEG')

    log.debug(f'Перед получением значения bytes')
    bts = img_bytes.getvalue()

    # вернём распознанную цифру, вероятность распознавания
    # и изображение, которое было на входе сети
    log.debug(f'Перед возвратом результата: {result[best]}')
    return {
        'number': result[best][0],
        'probability': result[best][1], 
        'image': bts
        }
