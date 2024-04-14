# 1. Write a Python Program to Find LCM?
hcf = 0
def hcf(a,b):
    if a>b:
        a,b = b,a
    for i in range(1,a+1):
        if a%i ==0 and b%i==0:
            hcf = i
    return hcf

def lcm(a,b):
    return (a*b)/(hcf(a,b))

print(lcm(18,24))


# 2. Write a Python Program to Find HCF?
hcf = 0
def hcf(a,b):
    if a>b:
        a,b = b,a
    for i in range(1,a+1):
        if a%i ==0 and b%i==0:
            hcf = i
    return hcf

print(hcf(20,100))

# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
num = int(input("enter the number"))
def binary():
    binary = bin(num).replace('0b', "")
    print(f'binary representation of {num} is {binary}')

def octal():
    octal = oct(num).replace('0o',"")
    print(f'octal representation of {num} is {octal}')

def hexadecimal():
    hexa = hex(num).replace('0x',"")
    print(f'hexadecimal representation of {num} is {hexa}')

binary()
octal()
hexadecimal()

# 4. Write a Python Program To Find ASCII value of a character?
char = input("enter the character")
ascii_val = ord(char)
print(f"ascii value of {char} is {ascii_val}")

# 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def div(a,b):
    return a/b

def multi(a,b):
    return a*b

def operation():
    print("Which operation you want to perform?")
    print("1.Addition\n2.Subtraction\n3.Division\n4.Multiplication")
    response=int(input("enter the response - "))
    num1 = int(input("enter first number - "))
    num2 = int(input("enter second number - "))
    if response == 1:
        print(addition(num1,num2))
    elif response ==2:
        print(subtraction(num1,num2))
    elif response ==3:
        print(div(num1,num2))
    elif response ==
        print(multi(num1,num2))

operation()