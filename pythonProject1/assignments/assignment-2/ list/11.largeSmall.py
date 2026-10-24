l=[2,3,17,6,22,6,90]
large=l[0]
small=l[0]
for i in range(len(l)):
    if l[i]>large:
        large=l[i]

    if l[i]<small:
        small=l[i]
print("largest=",large)
print("smallest=",small)