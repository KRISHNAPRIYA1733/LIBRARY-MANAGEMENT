try:
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    result=a/b
    print(result)
except ArithmeticError:
    print("invalid operation!")