def minutes_to_hours(minutes):
    try:
         hours = int(minutes / 60)
         remmin = minutes % 60
         return """
         Hours : {hours}
         Minutes : {remmin}
         """.format(hours = hours, remmin = remmin)
    except TypeError:
         return "Please enter an integer."

print(minutes_to_hours(95))
