# l=lambda a,b:a if a>b else b
# print(l(939,3964))

l=lambda x,y,z:x if x>y and x>z else y if y>x and y>z else z
print(l(20,399,32))