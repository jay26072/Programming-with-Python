# 6.Write a program to print Fibonacci series between two user input. 

n1 = 0
n2 = 1

start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

print("Fibonacci Series between",start,"and",end,"is:")
for i in range(start, end+1): 
    # print(i)

    if( i <= 1): 
        next = i
    else:
        next = n1 + n2
        n1 = n2
        n2 = next
    if (next >= start and next <= end):
        print(next, end=" ")