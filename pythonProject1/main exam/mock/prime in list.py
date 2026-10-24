l = [12, 7, 19, 20, 25, 31, 42, 43]
for num in l:
    prime = True
    for i in range(2,num):
        if num%i==0:
            prime=False
    if prime:
        print(num)

