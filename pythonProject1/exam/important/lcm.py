def callcm(x,y):
    if x>y:
        great=x
    else:
        great=y
    while great>0:
        if great%x==0 and great%y==0:
            lcm=great
            break
        else:
            great+=1
    return lcm
x=int(input("num1"))
y=int(input("num1"))
print(callcm(x,y))