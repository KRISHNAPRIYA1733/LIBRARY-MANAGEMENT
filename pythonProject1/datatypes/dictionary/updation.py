employee={"id":123,"name":"nandhu","place":"kollam","company":"tcs","salary":30000}
employee["number"]=9645197590
# adding
print(employee)
# editing
employee["place"]="adoor"
print(employee)
# deleting one attribute
del employee["id"]
print(employee)
# clearing
employee.clear()
print(employee)
# deleting
del employee

