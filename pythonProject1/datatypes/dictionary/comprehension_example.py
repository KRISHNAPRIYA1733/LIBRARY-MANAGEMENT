student=["ammu","anu","varun","nithin","Adhi","geetha"]
new_list=[]
for i in student:
    if 'a' in i or 'A' in i:
        new_list.append(i)
print(new_list)

#....with comprehension.....
student=["ammu","anu","varun","nithin","Adhi","geetha"]
new_list=[i for i in student if 'a' in i or 'A' in i]
print(new_list)