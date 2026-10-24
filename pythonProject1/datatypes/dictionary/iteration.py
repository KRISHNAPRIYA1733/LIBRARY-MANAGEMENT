employee={"id":123,"name":"nandhu","place":"kollam","company":"tcs","salary":30000}
#for i in employee:    gets key only
#for i in employee.keys():   gets key only
#for i in employee.values():     gets values
for i in employee.items():
    print(i)
print(type(i))