def numbers(*numbers):
    #...built_in......
    #print(sum(numbers))
    #...without built-in funtion....
    sum=0
    for i in numbers:
        sum+=i
    print(sum)
numbers(1,4,3,2,6)