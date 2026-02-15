# Метод isalnum()
# Метод isalpha()
# Метод isdigit()
# Метод islower()
# Метод isupper()

print(1, '-' * 60, 'isalnum')
s1 = 'abc123'
s2 = 'abc$*123'
s3 = ''
print(s1, s1.isalnum())
print(s2, s2.isalnum())
print(s3.isalnum())

s1 = 'АнДрЕй'
s2 = '2026'
print(s1, s1.isalnum())
print(s2, s2.isalnum())

print(2, '-' * 60, 'isalpha')
s1 = 'ABCabc'
s2 = 'abc123'
s3 = ''
print(s1, s1.isalpha())
print(s2, s2.isalpha())
print(s3.isalpha())

print(3, '-' * 60, 'isdigit')
s1 = '1234567'
s2 = '123abc123'
s3 = ''
print(s1, s1.isdigit())
print(s2, s2.isdigit())
print(s3.isdigit())

print(4, '-' * 60, 'islower, isupper')
s1 = 'abc'
s2 = 'abc1$d'
s3 = 'Abc1$D'
print(s1, s1.islower())
print(s2, s2.islower())
print(s3, s3.islower())

print(''.isupper())
print('1234'.isupper())
print('+-*/'.isupper())
print('AB#%'.isupper())
