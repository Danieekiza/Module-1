# dict
my_dict = {'Petrov': 1990, 'Ivanov': 1991, 'Sidorov': 1992}
print(my_dict)
print(my_dict['Petrov'])
print(my_dict.get('Svetlova', 'Такого имени нет'))
my_dict.update({'Svetlova': 1993})
print(my_dict)
dict_0 = my_dict.pop('Petrov')
print(dict_0)
print(my_dict)
# set
my_set = {0, 2, 3, True, (1, 2, 3), False}
print(my_set)
my_set.add('Vova')
print(my_set)