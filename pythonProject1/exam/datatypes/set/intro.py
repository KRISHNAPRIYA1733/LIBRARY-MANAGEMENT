s={2,2,3,5,7,3,1}
s1={2,45,9,43,3,5,31}
length=len(s)
print("length of string one=",length)
n=input("enter a choice:\nA-union\nB-intersection\nC-difference\nD-syymetric difference\n")
if n=='A':
    print(s|s1)
elif n=='B':
    print(s&s1)
elif n=='C':
    print(s-s1)
elif n=='D':
    print(s^s1)
else:
    print("invalid")

