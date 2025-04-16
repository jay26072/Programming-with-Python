class Employee:
    def dataEmp(self,name,age):
        self.name=name
        self.age=age
    def showEmp(self):
        print(self.name)
        print(self.age)

e=Employee()
e.dataEmp("Jay",22)
e.showEmp()
