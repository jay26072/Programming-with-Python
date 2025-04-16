import os,sys

fname=input("Enter The FileName : ")

if os.path.isfile(fname):
    f=open(fname,'r')

else:
    print(fname + ' Does Not Exist')
    sys.exit()

print("File Contents are: ")
str=f.read()

print(str)
f.close()
