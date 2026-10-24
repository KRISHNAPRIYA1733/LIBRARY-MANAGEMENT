# prime number
# start=int(input("enter starting number:"))
# end=int(input("ending number:"))
# for i in range(start,end+1):
#     flag = 0
#     if i<2:
#         continue
#     for j in range(2,i):
#         if i%j==0:
#             flag=1
#     if flag==0:
#         print(i)


#checking prime number
# n=int(input("enter a number"))
# for i in range(2,n):
#     if n%i==0:
#         flag=1
#         break
#     else:
#         flag=0
# if flag==1:
#     print("not prime")
# else:
#     print("prime")


#armstrong
# n=int(input("enter a number:"))
# a=n
# sum=0
# while a>0:
#     digit=a%10
#     sum=sum+digit**3
#     a=a//10
# if sum==n:
#     print("armstrong")

n=5
for i in range(1,n+1):
    for j in range(1,i):
        if i==j:
            print("1",end=" ")
        else:
            print("0",end=" ")

    print()






















