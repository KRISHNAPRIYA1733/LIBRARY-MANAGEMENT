def bmi(weight,height):
    bmi1=weight/(height)** 2
    return bmi1
weight=float(input("ente your weight:"))
height=float(input("enter your height:"))
print("bmi=",bmi(weight,height))