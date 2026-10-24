# l = [10, 20, 30, 40, 50, 60, 70]
# even=[]
# for i in range(0,len(l),2):
#     even.append(l[i])
# print(even)

l = [12, 25, 18, 31, 44, 53, 60, 77, 82]
even=[]
for i in range(0,len(l),2):
    if l[i]%2==0:
        even.append(l[i])
print(even)