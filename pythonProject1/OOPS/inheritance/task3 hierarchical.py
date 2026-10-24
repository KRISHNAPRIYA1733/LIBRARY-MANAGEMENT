class Bank:
    def __init__(self):
        self.Bname=""
        self.branch=""
        self.ifsc=""
        self.Mname=""
        self.Cno=0
    def Bdata(self):
        self.Bname=input("Enter bank name       :")
        self.branch=input("enter branch name    :")
        self.ifsc=input("enter ifsc         :")
        self.Mname=input("enter manager name    :")
        self.Cno=int(input("enter contact number:"))
    def BDisply(self):
        print("-----------Bank details----------------")
        print("Enter Bank Name      :",self.Bname)
        print("Enter branch Name    :",self.branch)
        print("Enter ifsc name      :",self.ifsc)
        print("Manager Name         :",self.Mname)
        print("Contact Number       :",self.Cno)
class Saving_Account(Bank):
    def __init__(self):
        self.Ano=0
        self.cname=""
        self.bal=0
        self.mobile=0
        self.Irate=0
    def Sdata(self):
        self.Ano=int(input("enter account number     :"))
        self.cname=input("enter customer number      :")
        self.bal=int(input("enter balance                  :"))
        self.mobile=int(input("enter mobile number         :"))
        self.Irate=int(input("enter the interest rate:"))
    def Sdisplay(self):
        print("-----------Savings details----------------")
        print("Account Number          :",self.Ano)
        print("Customer name           :",self.cname)
        print("Balance                 :",self.bal)
        print("Mobile                  :",self.mobile)
        print("Interest rate           :",self.Irate)
class Current_Account(Bank):
    def __init__(self):
        self.acNumber=0
        self.customer_name=""
        self.Balance=0
        self.busName=""
    def Cdata(self):
        self.acNumber=int(input("enter account number:"))
        self.customer_name=input("enter customer name:")
        self.Balance=int(input("enter balance        :"))
        self.busName=input("enter business name      :")
    def Cdisplay(self):
        print("-----------Current_account details----------------")
        print("account number       :",self.acNumber)
        print("customer name        :",self.customer_name)
        print("balance              :",self.Balance)
        print("Bussiness Name       :",self.busName)
class Loan_account(Bank):
    def __init__(self):
        self.lno=0
        self.cname=""
        self.lamnt=0
        self.Irate=0
        self.ltype=""
        self.dur=""
    def Ldata(self):
        self.lno=int(input("enter loan number:"))
        self.cname=input("enter customer name:")
        self.lamnt=input("enter loan amount  :")
        self.Irate=int(input("enter interest rate:"))
        self.ltype=input("enter loan type     :")
        self.dur=input("enter duration        :")
    def Ldisplay(self):
        print("-----------Loan details----------------")
        print("Loan number       :",self.lno)
        print("Customer Name     :",self.cname)
        print("Loan amount       :",self.lamnt)
        print("Interest rate     :",self.Irate)
        print("Loan type         :",self.ltype)
        print("Duration          :",self.dur)
obj1=Saving_Account()
obj1.Bdata()
obj1.Sdata()
obj1.BDisply()
obj1.Sdisplay()

obj2=Current_Account()
obj2.Bdata()
obj2.Cdata()
obj2.BDisply()
obj2.Cdisplay()

obj3=Loan_account()
obj3.Bdata()
obj3.Ldata()
obj3.BDisply()
obj3.Ldisplay()