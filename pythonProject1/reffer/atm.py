def atm():
    correctpin=1234
    balance=10000
    try:
        pin=int(input("enter your pin-"))
        if pin!=correctpin:
            raise ValueError("incorrect pin")
        print("login successful")
        amount=int(input("enter amount to withdraw-"))
        if amount>balance:
            raise ValueError("insufficient balance!")
        balance=balance-amount
        print("withdrawal successful")
        print("remaining Balance-",balance)
    except Exception as e:
        print("error",e)
    finally:
        print("Tankyou for visiting us")
atm()