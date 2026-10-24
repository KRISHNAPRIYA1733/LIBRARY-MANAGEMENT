n1=int(input("enter numeric code:"))
n2=int(input("enter amount:"))
if n1==1 and n2>1000:
    discount=((n2*10)/100)
    x=n2-discount
    print("net amount=",x)
elif n1==2 and n2>100:
    discount=(n2*5/100)
    x=n2-discount
    print("net amount=",x)
elif n1==3 and n2>500:
    discount=(n2*10/100)
    x=n2-discount
    print("net amount=",x)
else:
    print("net amount",n2)
