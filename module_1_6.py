# dict
my_dict = {'Petrov': 1990, 'Ivanov': 1991, 'Sidorov': 1992}
print('my_dict:', my_dict)
print('Existing value:', my_dict['Petrov'])
print(my_dict.get('Svetlova', 'Такого имени нет'))
my_dict.update({'Svetlova': 1993, 'Orlova': 1989})
print('my_dict.v1:', my_dict)
orlova = my_dict.pop('Orlova')
print('Deleted value:', orlova)
print('my_dict.v2:', my_dict)
# set
print() # пустая строка
my_set = {0, 2, 3, True, (1, 2, 3), False} # 0 и False одинаковые значения. одному из них не место в my_set
print('my_set:', my_set)
my_set.add('Vova')
my_set.add(3.3)
print('my_set.v1:', my_set)
my_set.remove(3.3)
print('my_set.v2', my_set)
