# -*- coding: utf-8 -*-
import json
import pandas as pd
#  импортируем список первых 150 популярных слов.
from exelTojson.work_with_dict import list_of_150

#  делаем из списка словарь.Функция возвращает словарь.
def to_dict(list_of_150):
    my_dict = {element[0]: element[1] for element in list_of_150}
    return my_dict

#  присваиваем новое имя словарю.
new_dict_150 = to_dict(list_of_150)
print(new_dict_150)

# присваиваем json данные к новому офису
words_150_in_json = json.dumps(new_dict_150).encode('utf-8')

# создаем json файл ( одно непонятно, если открыть файл, то кодировка сработала )
with open('words_150_in_json_file.json', 'w', encoding='utf-8') as outfile:
    json.dump(new_dict_150, outfile, ensure_ascii=False)


