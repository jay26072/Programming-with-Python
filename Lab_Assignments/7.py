#7.write a program to print sum of all even numbers between given users.

s1 = int(input("Enter Starting numbers :"))
e2 = int(input("Enter Ending element :"))

sum = 0
for i in range(s1,e2+1):
    if(i%2==0):
        sum += i
print("The sum of all even number :",sum)
