l=[2, 3, 2, 5, 3, 2, 7]
# d={}
# for i in l:
#     if i not in d:
#         d[i]=l.count(i)
# print(d)
#
d={}
for i in l:
    if i not in d:
        d[i]=l.count(i)
print(d)