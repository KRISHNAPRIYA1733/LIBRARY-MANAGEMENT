s=input("enter a string:")
word=s.split()
for i in word:
    print(i[0].upper()+i[1:],end=" ")