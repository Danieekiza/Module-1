#strings
example = 'Привет от старых штиблет!!'
len_str = len(example) -1 # длина строки
half_len = len_str // 2 # половина строки
secnd_half = example[half_len:len_str] # вторая половина строки
parity = len(secnd_half) % 2 # проверка на четность
print('Исходная строка: "' + example + '"')
print('Первый символ строки: "' + example[0] + '"')
print('Последний символ строки: "' + example[-1] + '"')
print('Вторая половина строки: "' + secnd_half + '"; нечетность: ' + str(bool(parity)))
print('Строка наоборот: "' + example[::-1] + '"')
print('Каждый второй элемент строки: "' + example[1::2] + '"') # исправлено на каждый второй элемент
