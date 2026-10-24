largest=lambda  a,b,c:a if (a>b and a>c)  else b if (b>a and b>c) else c
print(largest(10,20,30))
# using max
largest=lambda a,b,c:max(a,b,c)
print(largest(10,90,30))
