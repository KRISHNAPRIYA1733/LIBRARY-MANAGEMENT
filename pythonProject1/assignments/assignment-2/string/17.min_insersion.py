def check(text):
    if len(text)<=1:
        return 0
    if text[0]==text[-1]:
        return check(text[1:-1])
    return 1+min(check(text[1:]),check(text[:-1]))
word=input("enter a string:")
print("minimum insersion=",check(word))