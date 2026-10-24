name= input("enter student name:")
physics=int(input("enter physics mark:"))
chemistry=int(input("enter chemistry mark:"))
biology=int(input("enter biology mark:"))
english=int(input("enter biology mark:"))
maths=int(input("enter maths mark:"))
total=physics+chemistry+biology+english+maths
percentage=(total/500)*100
print("total mark=",total)
print("percentage=",percentage)
if percentage>=90:
    print("A Grade")
elif percentage>=80:
    print(" B Grade")
elif percentage>=70:
    print("C Grade")
elif percentage>=60:
    print ("D Grade")
else:
    print("Failed....!")