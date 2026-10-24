s=input("enter a string:")
upper=lower=digit=special=0
for i in s:
    if  i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digit+=1
    else:
        special+=1
print("upper",upper)
print("lower",lower)
print("digit",digit)
print("special",special)
