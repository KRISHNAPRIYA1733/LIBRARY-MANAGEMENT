try:
    n=int(input("enter a number:"))
    m=int(input("enter another number:"))
    print(n/m)
except ZeroDivisionError:
    print("Cant divide by zero!")
except ValueError:
    print("please enter a valid integer!!")