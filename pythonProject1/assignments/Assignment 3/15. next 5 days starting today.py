from datetime import date,timedelta
today=date.today()
for i in range(5):
    next1=today+timedelta(days=i)
    print(next1)