l=["sky", "sun", "sky", "moon", "sky", "sun"]
most=""
count=0
for i in l:
    if l.count(i)>count:
        count=l.count(i)
        most=i
print(most)

