employee={"id":123,"name":"nandhu","place":"kollam","company":"tcs","salary":30000}
print(type(employee))
print(".....employee details......")
print("company id:",employee["id"])
print("name of the employee:",employee["name"])
print("company name:",employee["company"])
print("salary:",employee["salary"])
employee["name"]="anu"
print(employee)
employee.update({"company":"infosys"})
print(employee)
