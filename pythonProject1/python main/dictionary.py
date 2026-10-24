# d = {
#     'arun': 25,
#     'amal': 34,
#     'akhil': 26,
#     'anu': 21,
#     'meera': 34
# }
# new={}
# for name,mark in d.items():
#     if mark>25:
#         new[name]=mark
# print(new)

d = {
    'arun': 25,
    'amal': 34,
    'akhil': 26,
    'anu': 21,
    'meera': 34
}
even={}
for name,mark in d.items():
    if mark%2==0:
        even[name]=mark
print(even)
