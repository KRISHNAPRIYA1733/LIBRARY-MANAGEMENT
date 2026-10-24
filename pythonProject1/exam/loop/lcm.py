
def lcm1(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while greater>0:
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        else:
            greater+=1
    return greater
x=int(input("enter a number:"))
y=int(input("enter another number:"))
print(lcm1(x,y))
