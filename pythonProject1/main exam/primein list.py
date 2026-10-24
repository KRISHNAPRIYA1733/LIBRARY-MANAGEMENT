#prime in list
# l = [10, 3, 7, 12, 17, 20, 23, 25, 29]
# # for num in l:
# #     prime=True
# #     for i in range(2,num):
# #         if num%i==0:
# #             prime=False
# #     if prime:
# #         print(num)

#prime with limit
# n=int(input("enter value for n:"))
# m=int(input("enter ending:"))
# for num in range(n,m+1):
#     prime=True
#     for i in range(2,num):
#         if num%i==0:
#             prime=False
#             break
#     if prime:
        #print(num)

#check prime
# n=int(input("enter a number:"))
# flag=0
# for i in range(2,n):
#     if n%i==0:
#         flag=1
# if flag==1:
#     print("not prime")
# else:
#     print("prime")

#prime in list
# l = [10, 3, 7, 12, 17, 20, 23, 25, 29]
# for num in l:
#     prime=True
#     for i in range(2,num):
#         if num%i==0:
#             prime=False
#     if prime==True:
#         print(num)

#if prime
num=int(input("Enter a number:"))
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
    else:
        flag=0
if flag==1:
    print("not")
else:
    print("yes")