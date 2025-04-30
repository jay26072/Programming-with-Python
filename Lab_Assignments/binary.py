# 3.Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal

num = int(input('Enter Number : '))
decimal = num
binary = bin(num)
octal = oct(num)
hexadecimal = hex(num)


print("Binary Number : " , binary)
print("Octal Number : " , octal)
print("Decimal Number : " , decimal)
print("Hexadecimal Number : " , hexadecimal)
