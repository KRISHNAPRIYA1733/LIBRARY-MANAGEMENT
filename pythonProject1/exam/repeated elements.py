#repeated elements
# l=[1,34,5,66,2,3,3,2]
# for i in range(len(l)):
#     for j in range(i):
#         if l[i]==l[j]:
#             print(l[j])

#prime
# n=int(input("enter a num:"))
# flag=0
# for i in range(2,n):
#     if n%i==0:
#         flag=1
#         break
# if flag==1:
#     print("not prime")
# else:
#     print("prime")


# #fibonacci
# n=int(input("enter a limit:"))
# a=0
# b=1
# for i in range(n+1):
#     print(a)
#     c=a+b
#     a=b
#     b=c

#fibonacci function
def fib(x):
    a=0
    b=1
    for i in range(x):
        print(a)
        c=a+b
        a=b
        b=c
fib(5)







