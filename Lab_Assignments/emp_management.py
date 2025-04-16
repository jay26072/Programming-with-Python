import pickle

while("true"):
    print("1. Enter Data")
    print("2. Print Salary Slip for Employee Names.")
    print("3. Print Employee List for Given Department No")
    print("4. Print all Employee")
    ch=int(input("Enter Your Choice: "))

    if ch==1:
        fp=open("emp.txt","ab")
        data=[]

        while(True):
            print("Append Data")
            no=int(input("Enter Number: "))
            name=input("Enter Name: ")
            deptpno=int(input("Enter Department No: "))
            basic=int(input("Enter Basic Salary: "))
            da=int(input("Enter Da: "))
            hra=int(input("Enter HRA: "))
            con=int(input("Enter CON: "))
            list1=[no,name,deptno,basic,da,hra,con,"\n"]
            data.append(list1)
            
                       
