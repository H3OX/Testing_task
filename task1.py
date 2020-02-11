# Задание 1.
TODO = """
1) Отсортировать все имена в лексикографическом порядке
2) Посчитать для каждого имени алфавитную сумму – сумму порядковых номеров букв (MAY: 13 + 1 + 25 = 39)
3) Умножить алфавитную сумму каждого имени на порядковый номер имени в отсортированном списке 
    (индексация начинается с 1). Например, если MAY находится на 63 месте в списке, то результат 
    для него будет 63 * 39 = 2457.
4) Просуммировать произведения из п. 3 для всех имен из файла и получить число. 
    Это число и будет ответом.
"""
import string
import numpy as np

# Функция переводит имя в последовательность чисел
def conversion(word):
    return [alphabet_numbers[x] for x in word]

# Открываем файл
file = open('names.txt', 'r')

# Английский алфавит
letters = list(string.ascii_uppercase)

# Переводим список имен в удобный для работы вид
names = [x.replace("\"", '') for x in list(sorted(file.read().split(',')))]

# Создание словаря пар буква: номер в алфавите
alphabet_numbers = {letters[x]: x + 1 for x in range(len(letters))}

# Второй пункт 
alphabetic_sum = [np.sum(conversion(x)) for x in names]

# Третий пункт
n_3 = [alphabetic_sum[x] * (x + 1) for x in range(len(alphabetic_sum))]
#print(f'Number: 51, Name: {names[50]}, a.sum: {alphabetic_sum[50]}, n3: {n_3[50]}')

# Четвертый пункт
print(np.sum(n_3))