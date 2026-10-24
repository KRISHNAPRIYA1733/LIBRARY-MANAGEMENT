# create a bank account class
# private attributes:
#     account nmuber
#     balance
# create methods:
#     deposite()
#     withdraw()
#     display_balance()
#
# access balance only trough methods
class Bankaccount:
    def __init__(self):
        self.name=""
        self.branch=""
        self.__AccNo=0
        self.__balance=0
    def Data(self):
        self.name=input("enter bank name:")
        self.branch=input("enter branch name:")
        self.__AccNo=int(input("enter account number:"))
        self.__balance=int(input("enter balance:"))
    def Display(self):
        print("Bank:",self.name)
        print("Branch:",self.branch)
        print("Account Number:",self.__AccNo)
        print("Balance:",self.__balance)
    def Deposit(self):
        amount=int(input("Enter amount to deposite:"))
        self.__balance=self.__balance+amount
        print("Amount deposited successfully....")
    def Withdraw(self):
        amount=int(input("Enter withdrawal amount:"))
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            print("withdrawal successfull....")
        else:
            print("Insufficient Balance!")
    def  display_balance(self):
        print("Account Balance:",self.__balance)
obj=Bankaccount()
obj.Data()
while True:
    print("1.Deposite","\n2.Withdraw","\n3.Check balance","\n4.Exit")
    c=int(input("Enter your choice:"))
    if c==1:
        obj.Deposit()
    elif c==2:
        obj.Withdraw()
    elif c==3:
        obj.display_balance()
    elif c==4:
        print("Thankyou")
        break

