import datetime 


time_str = "7:20"

hour_str = time_str[0:2]
minute_str = time_str[3:5]

hour = int(hour_str)
minute = int(minute_str)

time_object = datetime.time(hour=hour, minute=minute)
time_delta = datetime.timedelta(hours=time_object.hour, minutes=time_object.minute)

print(time_delta)
