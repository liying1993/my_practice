import datetime

now = datetime.datetime.now()
now_time = datetime.datetime.time(now)
morning_time = datetime.time(9, 0, 0, 0)
night_time = datetime.time(18, 0, 0, 0)
if not now_time >morning_time and now_time<night_time:
    print("bumanzu")
else:
    print("manzu")
