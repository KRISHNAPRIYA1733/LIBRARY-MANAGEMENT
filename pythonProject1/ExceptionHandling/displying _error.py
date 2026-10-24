try:
    n=int(input("enter a number:"))
    m=int(input("enter another number:"))
    print(n/m)
except Exception as e:
    print("Error!!",e)