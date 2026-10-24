s=input("enter a string:")
result=""
for i in s:
    if i not in result:
        result+=i
print("string after removing duplicates:",result)