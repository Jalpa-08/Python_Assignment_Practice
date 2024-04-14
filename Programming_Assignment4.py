# 1. Write a Python Program to Find the Factorial of a Number?
# num = int(input("enter the number"))
# fac = 1
# for i in range(1,num+1):
#     fac = fac*i
# print(fac)

# 2. Write a Python Program to Display the multiplication Table?
# num = int(input("enter the number for which multiplication table has to be displayed"))
# for i in range(1,11):
#     print(f'{num}*{i} = {num*i}')

# 3. Write a Python Program to Print the Fibonacci sequence?

# a = int(input("enter the first number"))
# b = int(input("enter th second number"))
# l = [a,b]
# seq = int(input("enter how many times you want to iterate the series"))
# for i in range(1,seq):
#     c = l[-1]+l[-2]
#     l.append(c)
#     a = l[-2]
#     b = l[-1]
# print(l)

# 4. Write a Python Program to Check Armstrong Number?
# num = int(input("enter the number"))
# pow = len(str(num))
# sum = 0
# for i in range(0,pow):
#     sum = sum + int(str(num)[i])**pow
# if sum == num:
#     print("entered number is an armstrong number")
# else:
#     print("number is not an armstrong number")

# 5. Write a Python Program to Find Armstrong Number in an Interval?
# interval = int(input("enter the number"))
# l = []
# for i in range(0,interval+1):
#     pow = len(str(i))
#     sum = 0
#     for j in range(0,pow):
#         sum = sum + int(str(i)[j])**pow
#     if sum==i:
#         l.append(i)
#
# print(l)

# 6. Write a Python Program to Find the Sum of Natural Numbers?
n=int(input("enter for how much numbers you want to know the sum"))
sum = (n*(n+1))/2
print(f"the sum of first {n} is {sum}")


