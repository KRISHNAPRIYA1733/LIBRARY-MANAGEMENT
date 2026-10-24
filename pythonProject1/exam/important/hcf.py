def calhcf(x,y):
    if x<y:
        small=x
    else:
        small=y
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
x=int(input("num1"))
y=int(input("num1"))
print(calhcf(x,y))
