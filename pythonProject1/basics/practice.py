#.......printing * using  nested loops
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print("* ",end="")
#     print()

#.......printing prime numbers
# n=int(input("enter starting point:"))
# m=int(input("enter ending point:"))
# for num in range(n,m+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)

#......numbers divisible by 5
# n=int(input("enter a limit:"))
# for i in range(n):
#     if i%5==0:
#         print(i)

#.......sum of all even numbers
# n=int(input("enter the limit:"))
# sum=0
# for i in range(2,n+1):
#         if i%2==0:
#            print(i)
#            sum=sum+i
# print(sum)

#.........star pattern decreasing
# n=int(input("enter the limit:"))
# for i in range(n+1,0,-1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()

n=int(input("enter a limit"))
for i in range(1,n+1):
    for j in range(1,2*n):
        if j==n-i+1 or j==n+i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()






















