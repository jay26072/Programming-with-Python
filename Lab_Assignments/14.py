import pickle

while True:
    print("\n1. Enter Data")
    print("2. Print Salary Slip for given Employee Number")
    print("3. Print Employee List for given Department Number")
    print("4. Print All Employees")
    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        with open("emp.txt", "ab") as f:
            while True:
                print("\nEnter Employee Data")
                no = input("Enter Emp Number: ")
                name = input("Enter Emp Name: ")
                deptno = input("Enter Dept Number: ")
                basic = input("Enter Basic Salary: ")
                hra = input("Enter HRA: ")
                da = input("Enter DA: ")
                con = input("Enter Conveyance: ")

                list1 = [no, name, deptno, basic, da, hra, con]
                pickle.dump(list1, f)

                ch1 = input("Enter Y to add more or N to exit: ")
                if ch1.lower() == 'n':
                    break

    elif ch == 2:
        try:
            with open("emp.txt", "rb") as f:
                empno = input("Enter Emp Number: ")
                found = False
                print("\nBasic\tDA\tHRA\tConveyance")
                while True:
                    try:
                        r = pickle.load(f)
                        if r[0] == empno:
                            print(r[3], "\t", r[4], "\t", r[5], "\t", r[6])
                            found = True
                    except EOFError:
                        break
                if not found:
                    print("Employee Not Found")
        except FileNotFoundError:
            print("File Not Found")

    elif ch == 3:
        try:
            with open("emp.txt", "rb") as f:
                deptno = input("Enter Department Number: ")
                found = False
                print("\nEmpNo\tName\tDeptNo\tBasic\tDA\tHRA\tConveyance")
                while True:
                    try:
                        r = pickle.load(f)
                        if r[2] == deptno:
                            print("\t".join(r))
                            found = True
                    except EOFError:
                        break
                if not found:
                    print("No Employees Found in this Department")
        except FileNotFoundError:
            print("File Not Found")

    elif ch == 4:
        try:
            with open("emp.txt", "rb") as f:
                print("\nEmpNo\tName\tDeptNo\tBasic\tDA\tHRA\tConveyance")
                while True:
                    try:
                        r = pickle.load(f)
                        print("\t".join(r))
                    except EOFError:
                        break
        except FileNotFoundError:
            print("File Not Found")

    else:
        print("Invalid Choice")

    ch2 = input("\nDo You Want To Continue (Y/N)? ")
    if ch2.lower() == 'n':
        break