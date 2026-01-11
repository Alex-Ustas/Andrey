# print('Python_крутой_язык!')
#
# print('Python', 'крутой', 'язык', sep='_', end='')
# print('!')
#
# print('Python', 'крутой', 'язык', '!', sep='_')
# print('Python', 'крутой', 'язык!', sep='_', end='!\n')
# print('Python_', 'крутой_', 'язык!', sep='', end='')

# a = 17 // (23 % 7)
# b = 34 % a * 5 - 17 // 2 ** 2
# print(a, b)
# print(a * b)

# word = input()
# if word == 'Python':
#     print('Yes')
# print('No')

# num = int(input())
# last_digit = num % 10    # последняя цифра числа
# first_digit = num // 10  # первая цифра числа
# if last_digit == first_digit:
#     print('ДА')
# else:
#     print('НЕТ')

# age = int(input())
# if 3 <= age <= 10:
#     print('Вы ребёнок')

# print(float('5'))
# #print(float('5 + 5'))
# print(int('5'))
# #print(int('5.7'))
# a = '5.7'
# print(abs(float(a)))
# # print(abs(a))
#
# n = ord('я') - ord('а') + 1
# print(n)
# print(ord('я'), ord('a'))
# print(ord('а'), ord('А'))
# z = 'a' == 'а'
# print('a' == 'а')

# text = '''Python is an interpreted, high-level, general-purpose programming language.
# Created by Guido van Rossum and first released in 1991, Python design
# philosophy emphasizes code readability with its notable use of significant whitespace.'''
# print(text)
# print('-' * 60)
#
# k = range(5, 11, -3)
# print('\nРезультат:', ', '.join(map(str, k)))

# for i in range(10, 100):    # перебираем числа от 10 до 99
#     if i % 10 == 7:         # используем остаток от деления на 10
#         print(i)

# for i in range(5, 0, -1):
#     print(4, 3, end=' ')
# print('Взлетаем!!!')
#
# total = 0
# counter = 0
# even = 0
# greater_than_6 = 0
#
# for i in range(10, 4, -1):
#     total += i
#     counter = counter + 1
#     last = i
#
#     if i % 2 == 0:
#         even += 1
#     if i > 6:
#         greater_than_6 = greater_than_6 + 1
# print(total, counter, even, greater_than_6)

found = False  # пока не нашли
while not found:  # пока found == False
    item = input("Что нашёл? ")
    if item == "ключ":
        found = True  # нашли! цикл закончится
        print("Ура, ключ найден!")
    else:
        print(item, "- это не ключ, ищем дальше...")
# открываем дверь и переходим к следующему сюжету
print("Открываем дверь...")
