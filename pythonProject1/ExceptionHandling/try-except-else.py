try:
    n=int(input("enter a number:"))
    m=int(input("enter a another number:"))
    print(n/m)
except Exception as e:
    print("error",e)
else:
    print("successfully completed")