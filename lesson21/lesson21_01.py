# Напишите функцию draw_box(), которая выводит звёздный прямоугольник с размерами 8×10 в соответствии с образцом:
# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********

def draw_line(x):
    print('*' * x)

def draw_box(y, z):
    draw_line(y)
    for i in range(z - 2):
        print('*', ' ' * (y - 2), '*', sep='')
    draw_line(y)


draw_box(8, 10)
