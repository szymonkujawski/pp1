def avg_speed(distance,hours,minutes):
    hrstomin = hours*60
    allminutes = hrstomin+minutes
    allhours = allminutes/60

    avrgspeed = distance/allhours
    return round(avrgspeed, 2)


distance = int(input("distance: "))
hours = int(input("hours: "))
minutes = int(input("minutes: "))

print(avg_speed(distance,hours,minutes))