def atm():
    correctpin=1234
    balance=30003
    try:
        pin=int(input("enter pin:"))
        if pin!=correctpin:
            raise ValueError("incorrect pin")
        print("successful login")
        amount=int(input("enter amount to withdraw"))
        if amount>balance:
            raise ValueError("insufficient balance")
        balance-=amount
        print("successful")
        print("balance=",balance)
    except Exception as e:
        print("error",e)
    finally:
        print("Thankyou")
atm()