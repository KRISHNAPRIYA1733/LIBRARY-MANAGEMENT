minimum=lambda a,b,c:min(a,b,c)
print(minimum(40,10,60))
#without min
minimum=lambda a,b,c:a if a<b and a<c else b if b<a and b<c else c
print(minimum(40,22,5))