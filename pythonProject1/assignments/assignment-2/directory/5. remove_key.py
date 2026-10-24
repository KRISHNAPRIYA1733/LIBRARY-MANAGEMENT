d={1:20,2:30,3:40}
s=int(input("enter a key to remove:"))
if s in d:
    del d[s]
    print(d)
else:
    print("key not found")
