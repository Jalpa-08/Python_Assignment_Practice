# 1. Write a Python program to convert kilometers to miles?
km = float(input('enter the kilometer you want to convert to miles- '))
miles = 0.621371*(km)
print(f'total miles is {miles}')

# 2. Write a Python program to convert Celsius to Fahrenheit?
Celsius = float(input('enter the temperature you want to convert to farenheit- '))
Farenheit = 32 + (Celsius)*9/5
print(f'Temperature in Farenheit is {Farenheit}')

# 3. Write a Python program to display calendar?

import calendar
year = 2023
month = 5

print(calendar.month(year,month))

# 4. Write a Python program to solve quadratic equation?
import cmath
# quadratic equation is of the form a*(x**2) + b*x + C
a = int(input("enter a"))
b = int(input('enter b'))
c = int(input('enter c'))
# calculating discriminant
d = (b**2 - 4*a*c)
if d == 0:
    x = (-b) / (2 * a)
    print(f'the equation has only one root which is {x}')
else:
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    print(f'two solutions of the given equation would be {x1},{x2}')


# 5. Write a Python program to swap two variables without temp variable?
a = 10
b = 20
a,b = b,a
print(f'swaped value of a is {a}')
print(f'swaped value of b is {b}')