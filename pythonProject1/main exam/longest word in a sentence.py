s="Python is very interesting"
long=""
word=s.split()
for i in word:
    if len(i)>len(long):
        long=i
print(long)
