def example1():
    print(2 + 3)
    print(2 + 3)
    print(2 + 3)
    print(2 + 3)

example1()
print(0, '-' * 60)

def example2():
    pass

example2()

def example(n, m):
    print(n + m)


example(3, 2)


def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)

draw_box(3, 14)
print(0, '-' * 60)

def print_hello(n):
    print('Hello' * n)


print_hello(5)


def print_hello2(text, n):
    print(text * n)


print_hello2('Андрей', 6)


def draw_box(height, width):
    height = 2
    width = 10
    for i in range(height):
        print('*' * width)

n = 5
m = 7
draw_box(n, m)
print(n, m)

