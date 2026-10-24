try:
    n=int(input("enter a number:"))
    result=100/n
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("enter a valid number!")
else:
    print("Result is",result)
finally:
    print("Division completetd.....")