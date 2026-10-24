l=[10, 25, 7, 40, 18]
large=l[0]
second=l[1]
for i in l:
    if i>large:
        second=large
        large=i
    elif i>second and i!=large:
        second=i
print(second)
