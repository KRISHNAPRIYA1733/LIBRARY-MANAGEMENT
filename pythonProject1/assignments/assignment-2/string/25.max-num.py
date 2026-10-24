s="hello good morning"
word=s.split()
long=word[0]
for i in word:
    if len(i)>len(long):
        long=i
print("longest word:",long)
