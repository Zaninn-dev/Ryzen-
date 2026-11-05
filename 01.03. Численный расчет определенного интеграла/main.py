
from math import cos, sin

while True:
    a = float(input('Введите нижний предел интегрирования a: '))
    b = float(input('Введите верхний предел интегрирования b: '))
    dx = float(input('Введите шаг интегрирования dx: '))

    s = 0
    x = a

    while x <= b:
        s += (cos(x) + sin(5 * x)) * dx
        x += dx

    print(f'\nРезультат: \n')

    print(f'Значение интеграла    {s:g} \n')

    print(f'---------------------------------------- \n')







