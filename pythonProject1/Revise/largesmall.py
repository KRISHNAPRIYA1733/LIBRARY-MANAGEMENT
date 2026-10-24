l=[1,23,45,67,43,43,2,6]
large=l[0]
small=l[0]
for i in l:
    if i>large:
        large=i
    elif i<small:
        small=i
print("large=",large)
print("small=",small)