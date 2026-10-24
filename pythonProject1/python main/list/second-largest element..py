l = [12, 45, 7, 89, 34, 56, 23, 78]
large=0
second=0
for i in l:
    if i>large:
        second=large
        large=i
    elif i>second and i!=large:
        second=i
print(second)
