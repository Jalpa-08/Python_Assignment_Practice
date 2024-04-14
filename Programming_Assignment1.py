# 1. Write a Python program to print &quot;Hello Python&quot;?
print("Hello Python")

# 2. Write a Python program to do arithmetical operations addition and division.?
x = 10
y = 20
add = x+y
div = x/y
print(f'{x}+{y} = {add}')
print(f'{x}/{y} = {div}')

# 3. Write a Python program to find the area of a triangle?

a = int(input("enter the length of the side of the triangle - "))
b = int(input("enter the length of the side of the triangle - "))
c = int(input("enter the length of the side of the triangle - "))
area = 0.5*(a+b+c)
print(f'area of the given triangle is {area}')

# 4. Write a Python program to swap two variables?

a = 10
b = 20
a,b = b,a
print(f'swaped value of a is {a}')
print(f'swaped value of b is {b}')

# 5. Write a Python program to generate a random number?

import numpy as np
print(np.random.randint(90,100))