#....  Number Pyramid in Python
n=int(input("enter a number:"))
for i in range(1,n+1):
   for s in range(n-i):
      print(" ",end=" ")
   for j in range(i):
      print(j+1,end=" ")
   for j in range(i-1,0,-1):
      print(j,end=" ")
   print()
