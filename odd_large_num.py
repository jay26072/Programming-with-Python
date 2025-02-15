# 5.Write a program to enter 10 numbers from user and find the largest odd number from them.

i = 0  
num = 0  
maximum = 0
N = 10  
while (i < N):
    num = int(input("Enter your number: "))
    if (num % 2 != 0):
        if (num > maximum):
            maximum = num
    i += 1
print("The maximum ODD number :", maximum)