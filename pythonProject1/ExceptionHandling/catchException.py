try:
    n=int(input("enter a number:"))
    b=int(input("enter another number:"))
    print(n/b)
except ZeroDivisionError:
    print("cant divide by zero")