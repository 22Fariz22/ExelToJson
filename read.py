# -*- coding: utf-8 -*-
import jsonlines  # может потребоваться утсановка этого модуля

dict_goods = {}  # создаем пустой словарь.
with jsonlines.open('json_str.json') as reader:
    for obj in reader:  # циклом читаем json.
        dic = obj['GOOD_NAME']  # присваиваем колонку.
        dict_goods.update(dic)  # добавляем в словарь и получаем
                                # пронумерованный словарь с товарами.

if __name__ == '__main__':
    print(dict_goods)

# далее в файле work_with_dict работаем со словарем.

