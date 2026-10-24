a = [10, 20, 30, 40, 50]
b = [30, 40, 50, 60, 70]
common=[]
for i in a:
    for j in b:
        if i==j:
            common.append(i)
print(common)
