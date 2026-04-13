from datetime import datetime

d= datetime.now()

print("d", d)
print("datetime.today()", datetime.today())
print(d.strftime("%Y, %M, %d, %H:%M:%S"))
print(d.strftime("%y, %m, %d, %h:%m:%s"))

# module = datetime 
# list of python datetime format characers:
# %a - Weekday as locale’s abbreviated name. (e.g., Sun, Mon, ...)
# %A - Weekday as locale’s full name. (e.g., Sunday, Monday, ...)
# %b - Month as locale’s abbreviated name. (e.g., Jan, Feb, ...)
# %B - Month as locale’s full name. (e.g., January, February, ...)
# %c - Locale’s appropriate date and time representation. (e.g., Mon Sep 30 07:06:05 2013)
# %d - Day of the month as a zero-padded decimal number. (e.g., 01, 02, ..., 31)
# %H - Hour (24-hour clock) as a zero-padded decimal number. (e.g., 00, 01, ..., 23)
# %I - Hour (12-hour clock) as a zero-padded decimal number. (e.g., 01, 02, ..., 12)
# %j - Day of the year as a zero-padded decimal number. (e.g., 001, 002, ..., 366)# %m - Month as a zero-padded decimal number. (e.g., 01, 02, ..., 12)
# %M - Minute as a zero-padded decimal number. (e.g., 00, 01, ..., 59)
# %p - Locale’s equivalent of either AM or PM. (e.g., AM, PM)
# %S - Second as a zero-padded decimal number. (e.g., 00, 01, ..., 59)
# %U - Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. (e.g., 00, 01, ..., 53)
# %w - Weekday as a decimal number, where 0 is Sunday and 6 is Saturday. (e.g., 0, 1, ..., 6)
# %W - Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. (e.g., 00, 01, ..., 53)
# %x - Locale’s appropriate date representation. (e.g., 09/30/13)
# %X - Locale’s appropriate time representation. (e.g., 07:06:05)
# %y - Year without century as a zero-padded decimal number. (e.g., 00, 01, ..., 99)
# %Y - Year with century as a decimal number. (e.g., 2013)


# custom datetime 
import datetime
# from datetime import datetime
# positional arguments 
# dob = datetime(year, month,date,hour,minute,second)
# keyword argument 
# dob = datetime(year=2020, month=12,....)

dob = datetime.datetime(2020,12,20,5,53,40)
print(dob)

# datetime to string conversion 
str = dob.strftime("%d-%m-%Y, %H:%M:%S")
print(str)

# string to datetime conversion 
s = "20-11-2021, 05:53:40"

d = datetime.datetime.strptime(s,"%d-%m-%Y, %H:%M:%S")

print(d)