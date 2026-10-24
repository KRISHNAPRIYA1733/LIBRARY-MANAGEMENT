class Calculator:
    def __init__(self):
        self.a=0
        self.b=0
    def data(self):
        self.a=int(input("enter 1st number:"))
        self.b=int(input("enter 2nd number:"))
    def addition(self):
        sum=self.a+self.b
        print("sum=",sum)
    def difference(self):
        diff=self.a-self.b
        print("Difference=",diff)
    def multiplication(self):
        mul=self.a*self.b
        print("Multiplication:",mul)
    def division(self):
        div=self.a/self.b
        print("Division=",div)
obj=Calculator()
obj.data()
while True:
    print("1.Addition","\n2.Differnce","\n3.Multiplication","\n4.Division","\n5.Exit")
    n=int(input("Enter a choice:"))
    if n==1:
        obj.addition()
    elif n==2:
        obj.difference()
    elif n==3:
        obj.multiplication()
    elif n==4:
        obj.division()
    else:
        print("Exit")
        break