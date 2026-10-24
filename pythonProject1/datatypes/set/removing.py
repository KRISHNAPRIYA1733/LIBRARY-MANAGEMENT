x={"python","html","css","javascript","django"}
x.remove("python")
print(x)
# x.remove("luminar")  #will get error
# print(x)
x.discard("python")
print(x)
x.discard("luminar")  # will not get error
print(x)