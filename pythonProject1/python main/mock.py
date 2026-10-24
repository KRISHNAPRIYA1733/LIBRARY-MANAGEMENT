#. Average from a string
# s = "ab12cd35ef7"
# sum=0
# count=0
# for i in s:
#     if i.isdigit():
#         i=int(i)
#         sum+=i
#         count+=1
# print("Average:",sum/count)

#First non-repeating character
# s = "aabbcdde"
# for i in s:
#     if s.count(i)==1:
#         print(i)
#         break


#Frequency
l = [4, 2, 4, 7, 2, 4, 9, 7, 7, 7]
#count=[]
# d={}
# for i in l:
#     if i not in d:
#         d[i]=l.count(i)
# print(d)
    # if i not in count:
    #     print(i,":",l.count(i))
    #     count.append(i)


#Second largest
# l = [15, 7, 32, 21, 9, 28]
# high=0
# sec=0
# for i in l:
#     if i>high:
#         sec=high
#         high=i
#     elif i>sec and i!=high:
#         sec=i
# print(sec)

#Common elements
# l1 = [2, 5, 7, 8, 10]
# l2 = [1, 2, 5, 9, 10]
# for i in l1:
#     if i in l2:
#         print(i)

#Prime numbers in a list
# l = [11, 15, 17, 20, 23, 27, 29, 30]
# for num in l:
#     prime=True
#     for i in range(2,num):
#         if num%i==0:
#             prime=False
#     if prime:
#         print(num)

#Palindrome number
# n=121
# temp=n
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum*10+digit
#     n=n//10
# if sum==temp:
#     print("yes")
# else:
#     print("no")


#Armstrong number
# n=153
# sum=0
# temp=n
# length=len(str(n))
# while n>0:
#     digit=n%10
#     sum=sum+digit**length
#     n=n//10
# if sum==temp:
#     print("yes")
# else:
#     print("no")


#Nth Fibonacci term
# def fib(n):
#     a=0
#     b=1
#     for i in range(n):
#         c=a+b
#         a=b
#         b=c
#     return a
# n=10
# print(fib(n))

#Prime function
# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             print("not prime")
#         else:
#             print("prime")
#         break
# n=3
# is_prime(n)

#Number pattern 1
# n=5
# for i in range(5):
#     for j in range(5):
#         if i==j:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()


#pattern 2
# s = "PYTHON"
# for i in range(len(s)):
#     print(s[0:i+1])


#OOP
# class person:
#     def __init__(self):
#         self.name="anu"
#         self.age=24
#     def display(self):
#         print("name",self.name)
#         print("age:",self.age)
# class student(person):
#     def __init__(self):
#         self.course="python"
#     def display(self):
#         print("course:",self.course)
# obj=student()
# obj.display()


#Exception Handling
# n=int(input("enter a num:"))
# m=int(input("enter a num:"))
# try:
#     division=n/m
# except ValueError:
#     print("not valid")
# except ZeroDivisionError:
#     print("not possible")
# finally:
#     print("program completed")






























