# def fib(n):
#     a=0
#     b=1
#     if a==1:
#         return a
#     if b==2:
#         return b
#     for i in range(3,n+1):
#         c=a+b
#         a=b
#         b=c
#     return b
# n=int(input("enter a no:"))
# print(fib(n))



# l=[2,4,5,6,2,4,6,6,2]
# occ=[]
# for i in l:
#     if i not in occ:
#         print(i,"-",l.count(i))
#         occ.append(i)



# l=["hi","hello","hi","mam","hello","hi"]
# count=0
# most=""
# for i in l:
#     if l.count(i)>count:
#         count=l.count(i)
#         most=i
# print(most)


#armstronglimit
# n=int(input("enter:"))
# m=int(input("enter:"))
# for num in range(n,m+1):
#     temp = num
#     sum=0
#     length=len(str(n))
#     while num>0:
#         digit=num%10
#         sum=sum+digit**length
#         num=num//10
#     if sum==temp:
#         print(sum)



#armstrong
# def arm(n):
#     temp=n
#     sum=0
#     length=len(str(n))
#     while n>0:
#         digit=n%10
#         sum=sum+digit**length
#         n=n//10
#     if sum==temp:
#         print("armstrong")
#     else:
#         print("not")
# n=int(input("enter number:"))
# arm(n)

# n=int(input("enter a no:"))
# temp = n
# sum = 0
# length = len(str(n))
# while n > 0:
#     digit = n % 10
#     sum = sum + digit ** length
#     n = n // 10
# if sum == temp:
#     print("armstrong")
# else:
#     print("not")

#disarrium
# n=int(input("enter:"))
# temp=n
# sum=0
# length=len(str(n))
# while n>0:
#     digit=n%10
#     sum=sum+digit**length
#     n=n//10
#     length-=1
# if sum==temp:
#     print("disarriu,")
# else:
#     print("not")

#harshad
# n=int(input("enter a number:"))
# sum=0
# for i in str(n):
#     sum=sum+int(i)
# if n%sum==0:
#     print("harshad")
# else:
#     print("not")


#pallindrome with numbers
# n=int(input("enter a number:"))
# temp=n
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum*10+digit
#     n=n//10
# if temp==sum:
#     print("pallindrome")


# l=[2,1,2,1,2,2,3,3]
# visit=[]
# for i in l:
#     if i not in visit:
#         print(i,"-",l.count(i))
#         visit.append(i)

#hcf
# def hcf1(x,y):
#     if x<y:
#         small=x
#     else:
#         small=y
#     for i in range(1,small+1):
#         if x%i==0 and y%i==0:
#             hcf=i
#     return hcf
# x=int(input("enter x:"))
# y=int(input("enter y:"))
# print(hcf1(x,y))

#lcm
def lcm1(x,y):
    if x>y:
        great=x
    else:
        great=y
    while great>0:
        if great%x==0 and great%y==0:
            lcm=great
            break
        else:
            great += 1
    return lcm
x=int(input("x:"))
y=int(input("y:"))
print(lcm1(x,y))




























