# 7.Write a Program sum of all even numbers between given user range.

start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

sum = 0

for i in range(start, end+1):
    if(i % 2 == 0):
        sum += i

print("Sum of all even numbers between",start,"and",end,"is:",sum)