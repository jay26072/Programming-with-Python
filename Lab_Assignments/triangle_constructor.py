class Triangle:
    def __init__(self,length,base):
        self.length=length
        self.base=base

    def calArea(self):
        area=(self.l*self.b)/2

    def showArea(self):
        print(self.area)


t=Triangle(5,2)
t.showArea()
    
