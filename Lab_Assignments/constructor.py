class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def showEmp(self):
        print(self.name)
        print(self.age)

e=Employee("Jay",22)
e.showEmp()
        
