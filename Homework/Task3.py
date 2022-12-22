# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int

import random
numbers = [1, 2, 3, 4, 5, 6, 7]
print('Первоначальный список:' + str(numbers))
result = random.sample(numbers, len(numbers))
print('Перемешанный список: ' + str(result))

