l=[2, 5, 2, 7, 5, 2, 9, 5, 5]
most=0
count=0
for i in l:
    if l.count(i)>count:
        count=l.count(i)
        most=i
print(most)