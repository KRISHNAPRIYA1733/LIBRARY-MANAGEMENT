# l = [4, 7, 2, 9, 4, 7, 8, 2, 5, 9]
# visit=[]
# for i in l:
#     if i not in visit:
#         visit.append(i)
# print(visit)















# l = [12, 5, 18, 5, 23, 12, 7, 18, 30]
# unique=[]
# new=[]
# for i in l:
#     if i not in unique:
#         unique.append(i)
#         if l.count(i)>1:
#             new.append(i)
# print(new)

# def dict(d):
#     for i in d.items():
#         print(i)
# d = {1: "a", 2: "b", 3: "d", 4: "e"}
# dict(d)



l = [10, 20, 10, 30, 40, 20, 50, 30, 60]
visit=[]
for i in l:
    if l.count(i)==1:
        visit.append(i)
print(visit)



