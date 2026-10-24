a=input("enter a sentence:")
b=input("enter a word to replace:")
c=input("enter new word")
word=a.split()
for i in word:
    if i==b:
        print(c,end=" ")
    else:
        print(i,end=" ")