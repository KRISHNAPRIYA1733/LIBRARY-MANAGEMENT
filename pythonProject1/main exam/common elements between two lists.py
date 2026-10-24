l1=[1, 2, 3, 4, 5]
l2=[3, 5, 7, 8, 2]
comm=[]
# for i in l1:
#     if i in l2:
#         comm.append(i)
# print(comm)
for i in l1:
    for j in l2:
        if i==j:
            comm.append(i)
print(comm)
