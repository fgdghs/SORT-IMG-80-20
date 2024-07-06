from pathlib import *
import os
from PIL import Image
p = Path('C:\\flower_photos')

out_p_test = Path('C:\\prepared_flower_photos\\test\\')
out_p_train = Path('C:\\prepared_flower_photos\\train\\')


for x in p.iterdir():
    # имя папки
    fold = str(x).split('\\')[-1]
    # Создание папки
    os.mkdir(str(out_p_train) + f'\\{fold}')
    os.mkdir(str(out_p_test) + f'\\{fold}')
    # Вычисление кол-во изображений для тренировки и проверки
    count_train = len(os.listdir(x)) * 80 // 100
    count_test = len(os.listdir(x)) * 20 // 100
    # Алгоритм сортировки
    for y in x.iterdir():
        if count_train > 0:
            img = Image.open(str(y))
            img.save(str(out_p_train) + f'\\{fold}' + '\\' + str(y).split('\\')[-1])
            count_train -= 1
        elif count_test > 0:
            img = Image.open(str(y))
            img.save(str(out_p_test) + f'\\{fold}' + '\\' + str(y).split('\\')[-1])
            count_train -= 1
            count_test -= 1






