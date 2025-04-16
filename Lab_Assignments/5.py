i=0
num=0
maximum=0
n=10
while i<n:
    num=int(input('Enter Number: '))
    if num%2!=0:
        if num>maximum:
            maximum=num
    i+=1 
print('Largest Odd number is: ',maximum)
