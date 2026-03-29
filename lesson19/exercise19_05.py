# На вход программе подаются число n, а затем – n песен, каждая на отдельной строке. Напишите программу, которая
# сортирует эти песни в алфавитном порядке и выводит каждую из них на отдельной строке.
#
# Формат входных данных
# На вход программе подаются натуральное число n, а затем – n строк.
#
# Формат выходных данных
# Программа должна вывести n песен, отсортированных в алфавитном порядке, каждую на отдельной строке.
#
# Пример:
# Входные данные:
# 3
# Il Volo – Grande Amore
# Drew Sarich – Gethsemane (I Only Want To Say)
# Il Volo – Canzone per te
# Выходные данные:
# Drew Sarich – Gethsemane (I Only Want To Say)
# Il Volo – Canzone per te
# Il Volo – Grande Amore
n = int(input())
c = []
for i in range(n):
    word = input()
    c.append(word)
c.sort()
print(*c, sep='\n')
