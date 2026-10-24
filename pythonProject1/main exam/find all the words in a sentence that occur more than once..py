s="python is easy and python is powerful"
dup=[]
words=s.split()
for i in words:
    if words.count(i)>1 and i not in dup:
        dup.append(i)
print(dup)


# s="hello good morning hello"
# dup=[]
# words=s.split()
# for i in words:
#     if words.count(i)>1:
#         dup.append(i)
# print(dup)
























