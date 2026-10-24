n=int(input("enter number of elements:"))
dup=[]
for i in range(n):
    num=int(input())
    dup.append(num)
l=[]
for i in dup:
    if i not in l:
        l.append(i)
print(l)

