# ...without comprehension
numbers=[1,2,3,4,5]
new_list=[]
for i in numbers:
    new_list.append(i**2)
print(new_list)
# with comprehension
numbers=[1,2,3,4,5]
new_list=[i**2 for i in numbers]
print(new_list)
