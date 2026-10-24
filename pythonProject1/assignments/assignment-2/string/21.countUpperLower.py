s="Hello Luminar"
upper=0
lower=0
for i in s:
    if i>='A' and i<='Z':
        upper+=1
    if i>='a' and i<='z':
        lower+=1
print("number of upper case:",upper)
print("number of lower case:",lower)