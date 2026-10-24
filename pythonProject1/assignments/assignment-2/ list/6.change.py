list1=[2,4,6,8,10]
k=int(input("enter value of k:"))
for i in range(k):
    l=list1[0]
    for j in range(len(list1)-1):
        list1[j]=list1[j+1]
    list1[len(list1)-1]=l
print(list1)