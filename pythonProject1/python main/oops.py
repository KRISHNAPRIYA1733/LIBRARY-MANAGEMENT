class BankAccount:
    def __init__(self):
        self.name="krishna"
        self.__acno=27374645367
        self.__balance=5000
    def display(self):
        print("name:",self.name)
        print("acno:",self.__acno)
        print("balance:",self.__balance)
    def deposit(self):
        amount=5000
        self.__balance=self.__balance+amount
        print("deposited successfully ")
    def withdraw(self):
        amount=3000
        if amount>self.__balance:
            print("insufficient balance")
        else:
            self.__balance=self.__balance-amount
        print("successfull and balance=",self.__balance)
    def balance(self):
        print("current balance:",self.__balance)
class SavingsAccount(BankAccount):
    def display(self):
        print("saving account")
        print("name:",self.name)
class CurrentAccount(BankAccount):
    def display(self):
        print("bank name: sbi")
obj=BankAccount()
obj.display()
obj.deposit()
obj.withdraw()
obj.balance()

obj2=SavingsAccount()
obj2.display()

obj3=CurrentAccount()
obj3.display()

