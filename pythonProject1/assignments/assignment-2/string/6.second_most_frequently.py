s=input("enter a string:")
first=0
second=0
char=""
for i in s:
    c=s.count(i)
    if c>first:
        second=first
        first=c
for i in s:
    c=s.count(i)
    if c==second:
        char=i
        break
print("second most frequent character:",char)
