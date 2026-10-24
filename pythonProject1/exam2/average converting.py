s="1467DFHkla8"
sum=0
count=0
for i in s:
    if i.isdigit():
        i=int(i)
        sum+=i
        count+=1
if count==0:
    print("invalid")
else:
    print("average=",sum/count)

# sum=0
# count=0
# for i in s:
#     if i.isdigit():
#         i=int(i)
#         sum+=i
#         count+=1
# if count==0:
#     print("invalid")
# print("average=",sum/count)