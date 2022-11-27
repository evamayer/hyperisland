from math import acos, sin, cos, radians
print("Enter the names, latitudes and longitudes of two points on the Earth in degrees!")
name1 = input("Point one name: ")
lat_1 = radians(float(input("Point one latitude: ")))
long_1 = radians(float(input("Point one longitude: ")))
name2 = input("Point two name: ")
lat_2 = radians(float(input("Point two latitude: ")))
long_2 = radians(float(input("Point two longitude: ")))

distance = 6371.01 * acos(sin(lat_1) * sin(lat_2) + cos(lat_1) * cos(lat_2) * cos(long_1-long_2))
speed = 740
duration = distance / speed
print("The distance between", name1, "and", name2, "is", round(distance, 2), "kilometers.")
print("A plane flying at", speed, "km/h would cover this distance in", round(duration, 2), "hours.")



