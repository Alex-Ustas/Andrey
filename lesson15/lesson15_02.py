# Метод count()
# Метод startswith()
# Метод endswith()
# Метод find(), rfind()
# Метод strip(), lstrip(), rstrip()
# Метод replace()

print(1, '-' * 60, 'count')
s = 'Маленькое дело лучше большого безделья'
print(s, '/ длина строки =', len(s))
print(s.count('о'), s.count('де'))
print(s[:20], '/', s.count('е', 0, 20))

print(2, '-' * 60, 'startswith')
s = '111 труд день, лень - тень'
print(s.startswith('111 труд'))
print(s.startswith('лень'))

print(3, '-' * 60, 'endswith')
s = 'труд день, лень - тень'
print(s.endswith('день'))
print(s.endswith('тень'))

print(4, '-' * 60, 'find, rfind')
s = 'abc abc def abc'
print(s)
print(s.find('abc'))
print(s.find('abc', 4))
print(s.rfind('abc'))
print(s.find('python'))
# print(s.index('python'))

print(5, '-' * 60, 'strip, rstrip, lstrip')
s = '   abc abc def abc     '
print('/', s, '/', sep='')
print('/', s.strip(), '/', sep='')
print('/', s.rstrip(), '/', sep='')
print('/', s.lstrip(), '/', sep='')
print()

s = '-+-+abc+-+-'
print(s)
print(s.strip('+-'))
print(s.rstrip('+-'))
print(s.lstrip('+-'))

print(6, '-' * 60, 'replace')
s = 'abc abc def abc'
print(s)
print(s.replace('abc', 'xyz'))
s.replace('abc', 'xyz')
print(s, ord('1'), ord('A'))

print(7, '-' * 60, 'mixed')
s = 'тРУД дЕнЬ, лЕнЬ - ТЕНЬ'
print(s)
print(s.find('лень'))
print(s.lower().find('лень'))
print(s.count('е'), s.count('н'))
print(s.lower().count('е'), s.upper().count('Н'))

s1 = s.lower()[:s.find(',')].replace('труд', 'лень')
s2 = s.lower()[s.find(','):].replace('лень', 'труд')
s = (s1 + s2).title()
print(s)
