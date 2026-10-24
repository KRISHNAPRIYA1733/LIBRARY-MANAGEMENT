# l = [12, 7, 45, 18, 23, 56, 91, 34, 10]
# odd=[]
# even=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("odd",odd)
# print("even",even)

#only the numbers that are greater than 10 AND divisible by 5.
l = [12, 5, 18, 7, 25, 30, 11, 40, 9]
new=[]
for i in l:
    if i>10 and i%5==0:
        new.append(i)
print(new)