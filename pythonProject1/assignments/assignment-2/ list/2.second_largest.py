l=[1,66,38,3,77,36,98]
large=l[0]
small=l[0]
for i in l:
    if i>large:
        large=i
    if i<small:
        small=i
second_large=small
second_small=large
for i in l:
    if i>second_large and i!=large:
        second_large=i
    if i<second_small and i!=small:
        second_small=i
print("second largest:",second_large)
print("second smallest:",second_small)