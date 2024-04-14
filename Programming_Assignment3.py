# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
num = int(input('enter the number'))
if num>0:
    print('Entered number is positive')
elif num == 0:
    print('Entered number is zero')
else:
    print('Entered number is negative')

# 2. Write a Python Program to Check if a Number is Odd or Even?
num = int(input('enter the number'))
if num%2==0:
    print("Entered number is even")
else:
    print("It is an odd number")

# 3. Write a Python Program to Check Leap Year?
y = int(input("enter the year"))
if y%4==0 and y%100!=0:
    print("it is a leap year")
elif y%4==0 and y%100==0 and y%400==0:
    print("it is a leap year")
else:
    print("the year is not a leap year")


# 4. Write a Python Program to Check Prime Number?
num  =int(input("enter the number to be checked"))
for i in range(2, num):
    if num % i == 0:
        print("it is not a prime number")
        break
else:
    print("this is a prime number")

# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?)
l=[]
for num in range(2,10000):
    for j in range(2,num):
        if num%j==0:
            break
    else:
        l.append(num)

print(l)