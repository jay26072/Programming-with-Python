# 3.Write a program to find the maximum and minimum of three numbers.

a=int(input("Enter Value of A: "))
b=int(input("Enter Value of B: "))
c=int(input("Enter Value of C: "))

# Maximum

if (a>b and a>c):
    print(a,"A is Maximum Number")
elif (b>a and b>c):
    print(b,"B is Maximum Number")
else:
    print(c,"C is Maximum Number")

# Minimum 

if (a<b and a<c):
    print(a,"A is Minimum Number")
elif (b<a and b<c):
    print(b,"B is Minimum Number")
else:
    print(c,"C is Minimum Number")