# Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать сумму его цифр.
#
# Пример:
# Входные данные:
# 12345
# Выходные данные:
# 15

def  print_digit_sum(num):
    k = sum([int(i) for i in str(num)])
    #print(sum(map(int, str(num))))
    print(k)

n = int(input())
print_digit_sum(n)
