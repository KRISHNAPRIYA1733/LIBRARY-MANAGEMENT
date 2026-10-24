s="Hello@123"
vowels=0
conso=0
digit=0
special=0
for i in s:
    if i in "aeiouAEIOU":
        vowels+=1
    elif i.isdigit():
        digit+=1
    elif i.isalpha():
        conso+=1
    else:
        special+=1
print("vowels",vowels)
print("consonents",conso)
print("digit",digit)
print("special",special)

