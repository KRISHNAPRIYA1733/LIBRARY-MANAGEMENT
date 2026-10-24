#1.first non-repeating character
# s="swiss"
# for i in s:
#     if s.count(i)==1:
#         print(i)
#         break

#3.Find the frequency of every element in:
# l=[2, 3, 2, 5, 3, 2, 7]
# count={}
# visit=[]
# for i in l:
#     if i not in visit:
#         count[i]=l.count(i)
#         visit.append(i)
# print(count)

#4.number is a palindrome.
# n=121
# temp=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if rev==temp:
#     print("pallindrome")
# else:
#     print("not a pallindrome")



#5.Print all prime numbers between two numbers entered by the user.
n=10
m=50
for num in range(10,50+1):
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime:
        print(num)