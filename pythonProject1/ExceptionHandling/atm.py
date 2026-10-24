def atm():
    correct_pin=1557
    balance=5500
    try:
        pin=int(input("Enter your pin:"))
        if pin!=correct_pin:
            raise ValueError("incorrect pin.....!")
        print("login Successfull")
        amount=int(input("enter amount to withdraw:"))
        if amount>balance:
            raise ValueError("insufficient balance....!")
        balance-=amount
        print("Withdrawal Successfull...")
        print("Current Balance-",balance)
    except Exception as e:
        print("Error",e)
    finally:
        print(".......Tankyou.......")
atm()
