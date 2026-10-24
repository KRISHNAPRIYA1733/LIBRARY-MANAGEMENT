def calcu_hcf(x,y):
    if x>y:
        small=x
    else:
        small=y
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
x=int(input("enter a number:"))
y=int(input("enter another number:"))
print(calcu_hcf(x,y))