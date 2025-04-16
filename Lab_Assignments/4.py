n=int(input('Enter numbers: '))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print('The number is palindrom')
else:
    print('The number is not palindrom')
