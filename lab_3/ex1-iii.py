import datetime

now = datetime.datetime.now()

yr = lambda x: x.year
mth = lambda x: x.month
dy = lambda x: x.day

year = yr(now)
month = mth(now)
day = dy(now)

print('Year ', year)
print('Month ', month)
print('Day ', day)

