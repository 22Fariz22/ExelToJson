# -*- coding: utf-8 -*-
import pandas as pd

# с помощью функции pandas.read_exсel() выбираем файл формата xlsx  и нужный лист.
excel_data_df = pd.read_excel('Dataset_холодильники.xlsx', sheet_name='Лист1')

#  преобразуем xlsx в json формат и присваиваем(имя любое).
#  После присваивания в папке появится json файл
json_str = excel_data_df.to_json()
with open('json_str.json', 'w', encoding='utf-8') as file:
    excel_data_df.to_json(file, force_ascii=False)

# далее в файле read.py преобразуем полученный здесь файл json в словарь.

