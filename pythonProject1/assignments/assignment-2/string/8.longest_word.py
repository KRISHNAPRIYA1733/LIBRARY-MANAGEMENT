s=input("enter a string:")
word=s.split()
longest=word[0]
for i in word:
    if len(i)>len(longest):
        longest=i
print("longerst:",longest)