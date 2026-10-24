#Write a Python program to find the elements that occur more than once in a list, and display each duplicate element only once.
l=[4, 2, 7, 4, 2, 9, 4, 7]
d={}
for i in l:
    if l.count(i)>1:
        d[i]=l.count(i)
print(d)
# d=[]
# l=[]
# for i in l:
#     if i not in d:
#         d.append(i)
#     else:
#         l.append(i)
# print(l)