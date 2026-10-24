def count_vowels(string):
    count=0
    vowels="aeiouAEIOU"
    for i in string:
        if i in vowels:
            count+=1
    return count
mystring=input("enter a string:")
print(count_vowels(mystring))


