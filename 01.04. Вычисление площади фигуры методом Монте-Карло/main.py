
from random import uniform
from math import pi

R1 = 1                    # радиус внутренней окружности
R2 = 2 * R1               # радиус внешней окружности
S0 = (R2*2)**2            # площадь квадрата
S1 = pi * R2**2 / 2 - pi * R1**2 / 2 + R2**2 - pi * R1**2 / 4         # точная площадь фигуры

while True:
    N = int(input('Введите количество точек N:   '))

    n = 0

    for _ in range(N):
        x = uniform(-R2, R2)
        y = uniform(-R2, R2)
        if (-R2 <= x <= 0 and 0 <= y <= R2 and  x**2 + y**2 <= R2**2 and x**2 + y**2 >= R1**2) or \
           (0 <= x <= R2 and -R2 <= y <= 0 and  x**2 + y**2 <= R2**2 and x**2 + y**2 >= R1**2) or \
           (-R2 <= x <= 0 and -R2 <= y <= 0 and x**2 + y**2 >= R1**2):
            n += 1

    s2 = S0 * (n / N)

    print('Результат:\n')

    print(f'Метод Монте-Карло       {s2:g} ед. кв.')
    print(f'Точное значение         {S1:g} ед. кв.')

    print('\n----------------------------------------\n')




