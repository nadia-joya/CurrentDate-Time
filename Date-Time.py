import datetime
now = datetime.datetime.now()
print("Current time is:")
print(now.strftime("%H:%M:%S"))
print("Current date is:")
print(now.strftime("%d-%m-%y"))