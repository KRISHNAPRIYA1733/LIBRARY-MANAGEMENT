s="Hello GoodMorning"
upper=0
lower=0
others=0
for i in s:
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower=lower+1
    else:
        others=others+1
print("upper case=",upper)
print("lower case=",lower)
print("others=",others)

