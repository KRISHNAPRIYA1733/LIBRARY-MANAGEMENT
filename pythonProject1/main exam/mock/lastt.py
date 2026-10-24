# s = "abc12def35gh7"
# sum=0
# count=0
# for i in s:
#     if i.isnumeric():
#         i=int(i)
#         sum+=i
#         count=count+1
# print("average=",sum/count)

l = [4, 2, 4, 7, 2, 4, 9, 7, 7, 7]
most=l[0]
least=l[0]
for i in l:
    if l.count(i)>most:
        most=i
    elif l.count(i)<least:
        least=i
print(most)
print(least)


