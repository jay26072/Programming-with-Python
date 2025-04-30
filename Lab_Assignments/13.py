n=int(input("Enter No.Of Records: "))
for i in range(0,n):
    
    roll=input("Enter Roll Number: ")
    name=input("Enter Name: ")
    data=[roll," ",name ,"\n"]

    try:
        fp=open("records.txt","a")
        fp.writelines(data)

    except Exception:
        fp=open("records.txt","w")
        fp.writelines(data)

    finally:
        fp.close()

#reading


try:
    fp=open("records.txt","r")
    #line=fp.readline()
    #print(line)

    lines=fp.readlines()
    print(lines)

except Exception as e:
    print(e)

finally:
    fp.close()
