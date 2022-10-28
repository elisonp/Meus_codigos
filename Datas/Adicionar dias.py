from datetime import date, timedelta
 
today_date = date.today()
 
print("CURRENT DAY : ", today_date)
 
td = timedelta(5)
print("AFTER 5 DAYS DATE WILL BE : ", today_date + td)
