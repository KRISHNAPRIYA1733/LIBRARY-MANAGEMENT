#armstrong without limit
# n=15
# temp=n
# sum=0
# length=len(str(n))
# while n>0:
#     digit=n%10
#     sum=sum+digit**length
#     n=n//10
# if sum==temp:
#     print("yes")
# else:
#     print("no")

#armstrong without limit
# n=100
# m=500
# for num in range(n,m+1):
#     sum=0
#     temp=num
#     length=len(str(num))
#     while num>0:
#         digit=num%10
#         sum=sum+digit**length
#         num=num//10
#     if sum==temp:
#         print(sum)

#harshad
# n=21
# sum=0
# for i in str(n):
#     sum=sum+int(i)
# if n%sum==0:
#     print("yes")
# else:
#     print("no")



# #disarrium
# n=175
# sum=0
# temp=n
# length=len(str(n))
# while n>0:
#     digit=n%10
#     sum=sum+digit**length
#     n=n//10
#     length=length-1
# if sum==temp:
#     print("disarrium")
# else:
#     print("not")

#pallindrome
# n=1211
# sum=0
# temp=n
# while n>0:
#     digit=n%10
#     sum=sum*10+digit
#     n=n//10
# if sum==temp:
#     print("yes")
# else:
#     print("no")

#pallindrome
# s="malayalam"
# rev=""
# for i in s:
#     rev=i+rev
# if rev==s:
#     print("yes")
# else:
#     print("no")

#fibanocci
n=10
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c




















