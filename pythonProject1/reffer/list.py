# l = [
#     {'empid': 100, 'name': 'arun', 'salary': 20000, 'email': 'arun@gmail.com'},
#     {'empid': 101, 'name': 'amal', 'salary': 25000, 'email': 'amal@gmail.com'},
#     {'empid': 102, 'name': 'anu', 'salary': 30000, 'email': 'anu@gmail.com'}
# ]
# m=[]
# s=[i['email'] for i in l]
# print(s)

#square root
# l = [25, 16, 9, 36]
# s=[ i**0.5 for i in l ]
# print(s)


#only even numbers
# l = [23, 46, 55, 11, 78, 90, 24]
# s=[i for i in l if i%2==0]
# print(s)

#greater
# l = [23, 46, 55, 11, 78, 90, 24]
# s=[i for i in l if i>50]
# print(s)

#first letter of each color
# l = ['red', 'green', 'blue', 'orange']
# s=[i[0] for i in l]
# print(s)

#length of each color.
# l = ['red', 'green', 'blue', 'orange']
# s=[len(i) for i in l]
# print(s)

#last character of each color.
# l = ['red', 'green', 'blue', 'orange']
# s=[i[-1] for i in l]
# print(s)

#reverse of every color
# colors = ['red', 'green', 'blue', 'yellow', 'black']
# s=[i[::-1] for i in colors]
# print(s)

#only the string values
# l = [23, 56, 12, 89, -34, -23, -67, -43, 9.7, 4.5, 'hello', 'world']
# s=[i for i in l if type(i)==str]
# print(s)


#only the positive numbers
# l = [23, 56, 12, 89, -34, -23, -67, -43, 9.7, 4.5, 'hello', 'world']
# s=[i for i in l if type(i)==int and i>0]
# print(s)

#length is greater than 6.
# fruits = ['apple', 'orange', 'pineapple', 'avocado', 'grapes']
# s=[i for i in fruits if len(i)>6]
# print(s)

#divisible by 3 from 1 to 100.
# s=[i for i in range(1,101) if i%3==0]
# print(s)

# n=int(input("enter the limit:"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

n=int(input("enter limit:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for s in range(i):
        print("*",end=" ")
    print()

