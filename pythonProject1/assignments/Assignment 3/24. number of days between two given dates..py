import datetime
n=input("enter first date:")
m=input("enter second date:")
date1=datetime.datetime.strptime(n,"%d/%m/%Y").date()
date2=datetime.datetime.strptime(m,"%d/%m/%Y").date()
print(date1)
print(date2)
difference=date2-date1
print("number of days between the days:",difference)