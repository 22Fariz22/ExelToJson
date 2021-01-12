# -*- coding: utf-8 -*-
import copy
from collections import Counter


#  импортируем наш полученный словарь
from exelTojson.read import dict_goods

dict_goods2 = copy.deepcopy(dict_goods)  # делаем копию импортируемого словаря
list_of_goods = []  #  создаем пустой список для заполнения слов

#  циклом формируем спискок(может так проще работать со строками чем со словарем)
for k,v in dict_goods2.items():
    list_of_goods.append(v.lower().replace(',', ' ').replace('.', ' ').
                         replace(';', ' ').replace('[', ''))
list_of_goods_2 = []
#  убираем все пробелы и добавляем все в новый список list_of_goods_2
for i in list_of_goods:
    list_of_goods_2.extend(i.split())


# подсчет частоты каждого слова в списке
c = Counter(list_of_goods_2)
list_of_150 = c.most_common(150)  # составляем список 150 популярных слов


if __name__ == '__main__':
    print(list_of_150)


