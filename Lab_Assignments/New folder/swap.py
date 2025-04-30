# 1.Swap two numbers without using third variable

a=int(input("Enter Value of A: "))
b=int(input("Enter Value of B: "))

print("\nBefore Swapping")
print("Value of A: ",a)
print("Value of B: ",b)

a=a+b
b=a-b
a=a-b

print("\nAfter Swapping")
print("Value of A: ",a)
print("Value of B: ",b)