# -*- coding: utf-8 -*-
import pandas as pd

# преобразуем эксель файл в обычный список(type list)

# с помощью функции pandas.read_exсel() выбираем файл формата xlsx
# и нужный лист.
ecxel_data_goods = pd.read_excel('Dataset_холодильники.xlsx', sheet_name='Лист1')

# создаем список товаров из GOOD_NAME .
list_of_good_name = ecxel_data_goods['GOOD_NAME'].tolist()
print(list_of_good_name)

