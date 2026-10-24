#area and perimeter
def area(x,y):
    area1=x*y
    return area1
def peri(x,y):
    perimeter=2*(x+y)
    return perimeter
x=int(input("enter length"))
y=int(input("enter bredth"))
print(area(x,y))
print(peri(x,y))