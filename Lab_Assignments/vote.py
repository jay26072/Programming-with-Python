# 8.Write a program to check whether a person is eligible to vote or not.
age=int(input("Enter your age: "))

if (age >= 18):
    msg="Eligible"

else:
    msg="Not Eligible"

print("You are",msg,"for Vote.")