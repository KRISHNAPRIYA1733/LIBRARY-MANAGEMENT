import re
sentence="hello ,hello good mornging,introduction to python"
x=re.findall("hello",sentence)
print(x)
print(len(x))