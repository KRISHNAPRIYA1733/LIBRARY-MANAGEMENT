l = [12, 45, 67, 23, 89]
high=l[0]
second=l[0]
for i in l:
    if i>high:
        second = high
        high=i
    elif i>second and i!=high:
        second=i
print(second)