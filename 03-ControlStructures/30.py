time = str(input("Enter time (24-hour format) (hh:mm): "))

hours = time[:2]
minutes = time[3:5]

hours = int(hours)
minutes = int(minutes)

if hours>=0 and hours<24 and minutes>=0 and minutes<60:
    if hours<=11:
        print(f"Time in 12-hour format: {hours}:{minutes}am")
    else:
        print(f"Time in 12-hour format: {hours-12}:{minutes}pm")
else:
    print(f"Invalid hour")