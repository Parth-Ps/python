import datetime
import calendar

today = datetime.date.today()
day_currrent_mon = calendar.monthrange(today.year, today.month)[1]
days_til_end_mon = day_currrent_mon = today.day
print(days_til_end_mon)
