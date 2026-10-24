try:
    a=int(input("enter a number:"))
    b=int(input("enter a number to divide:"))
    result=a/b
    print(result)
except ZeroDivisionError:
    print("zero division is not possible!")
except Exception as e:
    print("error!!",e)
finally:
    print("division completed...")