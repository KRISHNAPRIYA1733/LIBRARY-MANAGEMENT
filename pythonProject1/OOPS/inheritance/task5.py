class ATM:
    def __init__(self):
        self.acN0=0
        self.name=""
        self.bal=0
    def CreateAccount(self):
        print("-----account creation------")
        self.acN0=int(input("enter account number:"))
        self.name=input("eneter user name:")
        self.bal=int(input("enter balance"))
        print("Account Created.....")
    def deposit(self):
        print("--------Deposit----------")
        amount=int(input("Enter deposit amount:"))
        self.bal+=amount
        print("Amount deposited successfully...")
    def withdraw(self):
        print("------withdrawal--------")
        amount=int(input("enter amount to withdraw:"))
        if amount<=self.bal:
            self.bal-=amount
        else:
            print("insufficient balance:")
        print("withdrwn successfully......")
    def balanceCheck(self):
        print("Account Balance :",self.bal)
    def mini_statement(self):
        print("-------Balance---------")
        print("Account Holder name:",self.name)
        print(("Account number:",self.acN0))
        print(("balance:",self.bal))
obj=ATM()
while True:
    print("1.account creation","\n2.Deposit","\n3.withdraw","\n4.balancecheck","\n5.mini statement","\n6.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        obj.CreateAccount()
    elif choice==2:
        obj.deposit()
    elif choice==3:
        obj.withdraw()
    elif choice==4:
        obj.balanceCheck()
    elif choice==5:
        obj.mini_statement()
    elif choice==6:
        print("thankyou")
        break
    else:
        print("invalid option")






