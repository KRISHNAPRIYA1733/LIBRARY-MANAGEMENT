# l = [12, 45, 7, 89, 34, 12, 56, 7, 90]
# visit=[]
# new=[]
# for i in l:
#     if i not in visit:
#         visit.append(i)
#     else:
#         new.append(i)
# print(new)

l = [10, 20, 10, 30, 20, 40, 10]
visit=[]
new=[]
for i in l:
    if i not in visit:
        visit.append(i)
    else:
        new.append(i)
new=set(new)
new1=list(new)
print(new1)
