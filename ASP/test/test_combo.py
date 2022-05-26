from datetime import *
import pytz

local_time = pytz.timezone("Asia/Bangkok")
timeee = datetime.now(tz=local_time).strftime("%Y-%m-%d")
time_now = datetime.now(tz=local_time).strftime("%H:%M:%S")
# time_now = str(time())
time = str(
    time(
        hour=8,
        minute=10,
        second=0,
        tzinfo=local_time,
    )
)

if time_now < time:
    print("Time is less than 8:10:00")
    print(time_now)
    print(timeee)
else:
    print("Time is greater than 8:10:00")
    print(time_now)
    print(timeee)
