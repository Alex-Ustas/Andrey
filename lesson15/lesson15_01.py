# Метод capitalize()
# Метод swapcase()
# Метод title()
# Метод lower()
# Метод upper()

print(1, '-' * 60, 'capitalize')
s = 'лучше один раз сделать, чем сто раз отложить'
print(s.capitalize())

s = '1лучше один раз #@$^@%, чем сто раз @#%^&@#@'
print(s.capitalize())

print(2, '-' * 60, 'swapcase')
s = 'тРУД дЕнЬ, лЕнЬ - ТЕНЬ'
print(s.swapcase())

print(3, '-' * 60, 'title')
s = 'парамонов андрей евгеньевич'
print(s.title())

s = '%лучше.один 1раз сделать, чем сто раз отло2жить'
print(s.title())

print(4, '-' * 60, 'lower')
s = 'тРУД дЕнЬ, лЕнЬ - ТЕНЬ'
print(s.lower())

print(5, '-' * 60, 'upper')
s = 'тРУД дЕнЬ, лЕнЬ - ТЕНЬ'
print(s.upper())

print(6, '-' * 60, 'Notes')
song = 'the show must go on'
song.title()
print(song)

song = 'the show must go on'
song = song.title()
print(song)
