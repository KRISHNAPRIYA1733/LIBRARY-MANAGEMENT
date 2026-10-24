s=[2,4,5,7,5,3,5,6,7,222]
large=s[0]
for i in s:
    if i>large:
        large=i
print(large)