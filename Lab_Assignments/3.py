a=int(input("Enter first number A :"))
b=int(input("Enter second number B :"))
c=int(input("Enter second number C :"))

if(a>b and a>c):
     print("A is maximum",a)
else:
    if(b>c and b>a):
        print("B is maximum",b)
    else:
        print("C is greater",c)
        
if(a<b and a<c):
     print("A is minimum",a)
elif(b<c and b>a):
        print("B is minimum",b)
else:
        print("C is minimum",c)
    
