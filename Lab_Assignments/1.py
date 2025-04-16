#1.write a python proogram to swap two variable without using third variable(by user input).

a=int(input("Ente Value Of A :"))
b=int(input("Enter Value Of B :"))
print("\n")
print("Entered number A: ",a)
print("Entered number B: ",b)

print("\n")
print("swap numbers")
a=a+b 
b=a-b
a=a-b
print("a = ",a)
print("b = ",b)
