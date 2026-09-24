
from math import cos, sin, tan, log

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))

print('\n')

while True:
    x = float(input('x: '))

    if x <= a:
        y = cos(x) + sin(5 * x)
    elif a < x < b:
        y = abs(tan(0.2 * x)) + x
    elif x >= b: 
        y = sin(x) + log(x)

    print(f'y: {y:g}\n')





