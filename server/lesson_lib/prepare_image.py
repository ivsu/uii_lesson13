# выполняет поиск значимой части изображения и готовит изображения для подачи в сеть
# на вход подаётся фотография цифры с произвольной обрезкой и произвольного размера
# на выходе квадратное изображение белой цифры на чёрном фоне заданного размера
# 
# img - изображение (цветное или ч/б)
# size - размер, к которому нужно привести изображение
# lum_threshold - порог яркости, ниже которого пиксели будут сочтены за шум и обрезаны до чёрного
# verbose - признак вывода промежуточных изображений для отладки

# импорт файлов проекта
from . import logger

# загрузка стандартных библиотек
import numpy as np
from tensorflow.keras.utils import img_to_array, array_to_img

import matplotlib.pyplot as plt
import sys

log = logger.get(__name__)    

# def prepare_image(img, size, lum_threshold, log, verbose=0):
def prepare_image(img, size, lum_threshold, verbose=0):

    log.debug(f'Начало обработки')
    if verbose:
        plt.imshow(img)
        plt.show()

    # конвертируем цветное изображение в оттенки серого
    if img.mode != 'L': 
        img = img.convert('L')
    log.debug(f'Сконвертировано')

    # конвертируем в массив numpy и уберём ненужную ось слоя
    img = img_to_array(img)[..., 0]
    
    # выведем контрастность в светлой части на максимум и инвертируем яркость
    img = 255. - np.round(img / np.max(img) * 255., 0)

    if verbose:
        plt.imshow(img, cmap='gray')
        plt.show()
    
    # пожертвуем информацией в тёмных тонах,
    # сочтя её за шум, согласно переданному порогу обрезки
    img[img < lum_threshold] = 0

    if verbose:
        plt.imshow(img, cmap='gray')
        plt.show()

    # определим координаты границ изображения
    i = np.argwhere(img)
    ymin, ymax = np.min(i[:, 0]), np.max(i[:, 0])
    xmin, xmax = np.min(i[:, 1]), np.max(i[:, 1])
    # добавим пустое пространство по краям в 20% от размера значимой части изображения
    ymin = round(max(0, ymin - (ymax - ymin) * 0.2))
    ymax = round(min(img.shape[0], ymax + (ymax - ymin) * 0.2))
    xmin = round(max(0, xmin - (xmax - xmin) * 0.2))
    xmax = round(min(img.shape[1], xmax + (xmax - xmin) * 0.2))
    # значимая часть изображения
    img = img[ymin : ymax, xmin : xmax]

    if verbose:
        plt.imshow(img, cmap='gray')
        plt.show()

    # уменьшеним размер изображения до требуемого размера
    img = array_to_img(np.expand_dims(img, axis=-1))
    img.thumbnail((size, size))
    img = img_to_array(img)[..., 0]

    if verbose:
        plt.imshow(img, cmap='gray')
        plt.show()

    # размер значимой части изображения
    h, w = img.shape[0], img.shape[1]
    # матрица под новое квадратное изображение
    base = np.zeros((size, size))
    # сдвиг изображения в квадратной матрице
    dy, dx = round((size - h) / 2), round((size - w) / 2)
    # вставка изображения в квадратную матрицу
    base[dy : dy + h, dx : dx + w] = img

    return base
