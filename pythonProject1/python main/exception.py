balance=5000
pin=1234
try:
    pinno=int("enter pin number:")
    if pinno!=pin:
        raise ValueError("wrong")

