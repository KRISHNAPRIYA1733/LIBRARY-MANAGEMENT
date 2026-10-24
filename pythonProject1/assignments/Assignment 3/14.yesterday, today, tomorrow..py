from datetime import date,timedelta
today=date.today()
print("Today:",today)
print("Yesterday:",today-timedelta(days=1))
print("Tomorrow:",today+timedelta(days=1))