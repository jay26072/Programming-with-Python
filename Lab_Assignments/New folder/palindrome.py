# 4.Write a program to check whether a number is palindrome or not.

num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print(temp,"The number is a palindrome!")
else:
    print(temp,"The number isn't a palindrome!")

