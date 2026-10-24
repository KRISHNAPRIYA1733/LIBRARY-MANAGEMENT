s=input("enter a string:")
vowels=0
consonants=0
digits=0
space=0
special_charcter=0
for i in s:
    if i.isalpha():
        if i.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        space+=1
    else:
        special_charcter+=1
print("vowels=",vowels)
print("consontents=",consonants)
print("digits=",digits)
print("space=",space)
print("special characters=",special_charcter)
