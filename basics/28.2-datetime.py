from datetime import date, timedelta


# create a date object 
d = date(2023,12,25)

print(d)
print(d.year)
print(d.month)
print(d.day)

print(d.strftime("%Y/%B/%d"))
print(d.strftime("%d, %B, %Y"))

str = "20/5/2019"
print(date.strptime(str,"%d/%m/%Y"))
d = d.replace(day=15)
print(d)

# week day 
# Monday = 0, Sunday = 6

print(d.weekday()) 
# date arithmetic 

today  = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print(f"Yesterday: {yesterday}")
print(f"Today: {today}")
print(f"Tomorrow: {tomorrow}")

diff = tomorrow - yesterday
print(diff.days)
deadline = date(year=2026,month=4,day=30)
print((deadline - today).days)