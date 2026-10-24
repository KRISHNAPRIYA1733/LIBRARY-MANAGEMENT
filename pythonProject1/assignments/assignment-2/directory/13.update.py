d={1:20,2:30,3:40,7:92,9:23,5:43}
key=int(input("enter a key :"))
if key in d:
    value=int(input("enetr new key value:"))
    d[key]=value
    print(d)
else:
    print("key not exist")

