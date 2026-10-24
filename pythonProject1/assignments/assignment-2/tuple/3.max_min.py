tup=(1,5,7,3)
maximum=tup[0]
minimum=tup[0]
for i in tup:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print("maximum is",maximum)
print("minimum",minimum)
