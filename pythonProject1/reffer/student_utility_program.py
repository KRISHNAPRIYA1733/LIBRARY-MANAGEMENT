import math,random,datetime
print("1.find square root")
print("2.find factorial")
print("3.Roll dice\n4.show date and time\n5.exit")
n=int(input("enter a choice:"))
if n==1:
    m=int(input("enter a number:"))
    print(math.sqrt(m))
elif n==2:
    num=int(input("enter a number:"))
    print(math.factorial(num))
elif n==3:
    print(random.randint(1,6))
elif n==4:
    print(datetime.datetime.now())
else:
    print("exit")