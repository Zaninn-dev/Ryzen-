
from math import cos, sin, log
from random import uniform

while True:
    print('Для выбора метода интегрирования введите требуемое число:')
    print('1 - метод прямоугольников')
    print('2 - метод трапеций')
    print('3 - метод симпсона\n')
    choice = input()

    a = float(input('Введите нижний предел интегрирования a: '))
    b = float(input('Введите верхний предел интегрирования b: '))
    dx = float(input('Введите шаг интегрирования dx: '))

    N = int(input('Введите количество точек N: '))
    
    if choice == "1":                               # метод прямоугоников
        S = 0                 
        x = a 
        while x <= b:
            y1 = cos(x) + sin(5 * x)              
            y2 = sin(x) + log(x)                 
            y = y2 - y1                          
            ds = y * dx                          
            S += ds
            x += dx


    elif choice == "2":                             # метод трапеций
        S = 0           
        x = a

        while x <= b:
            y1 = cos(       x) + sin(5 * x)              
            y2 = cos(x + dx) + sin(5 * (x + dx))  
            ds1 = (y1 + y2) / 2 * dx              

            y1 = sin(x) + log(x)                  
            y2 = sin(x + dx) + log(x + dx)        
            ds2 = (y1 + y2) / 2 * dx              

            ds = ds2 - ds1                       

            S += ds
            x += dx

    elif choice == "3":                             # метод Cимпсона
        S = 0           
        x = a
        
        while x <= b:
            y1 = cos(x) + sin(5 * x)              
            y2 = cos(x + dx) + sin(5 * (x + dx))
            y3 = cos(x + 2 * dx) + sin(5 * (x + 2 * dx))
            ds1 = (dx / 3) * (y1 + 4 * y2 + y3)              

            y1 = sin(x) + log(x)                  
            y2 = sin(x + dx) + log(x + dx)
            y3 = sin(x + 2 * dx) + log(x + 2 * dx)
            ds2 = (dx / 3) * (y1 + 4 * y2 + y3)              

            ds = ds2 - ds1                       

            S += ds
            x += 2 * dx

    x = a

    min1 = cos(x) + sin(5 * x)
    max1 = sin(x) + log(x)

    steps = int((b - a) / dx) 
    
    for i in range(steps + 1):
        x = a + i * dx
        
        y1 = cos(x) + sin(5 * x)
        y2 = sin(x) + log(x)

        if y1 < min1:
            min1 = y1
        if y2 > max1:
            max1 = y2
             
    n = 0                                              
    i = 0
    
    while i < N:                                        # метод Монте-Карло 
        x = uniform(a, b)
        y = uniform(min1, max1)
        
        y1 = cos(x) + sin(5 * x)
        y2 = sin(x) + log(x)
        
        if y1 <= y <= y2:
            n += 1
            
        i += 1
            
    S0 = (b - a) * (max1 - min1)
    S1 = S0 * n / N


    print('Результат:\n')

    if choice == "1":
        print(f'Метод прямоугольников   {S:g} ед. кв.')
    if choice == "2":
        print(f'Метод трапеций          {S:g} ед. кв.')
    if choice == "3":
            print(f'Метод Симпсона       {S:g} ед. кв.')

    print(f'Метод Монте-Карло       {S1:g} ед. кв.')


    print('\n----------------------------------------\n')



















