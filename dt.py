import datetime

d = datetime.datetime.now()
print(d.year)
print(d.month)
print(d.day)

import datetime

d = datetime.datetime(2019, 5, 23)
print(d.strftime("%d/%m/%y"))
print(d.strftime("%d/%m/%Y"))
print(d.strftime("%a%m,/%d/%Y"))
