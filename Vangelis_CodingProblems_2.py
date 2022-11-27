miles_per_gallon = input("Please enter the fuel efficiency in miles-per-gallon: ")
miles_per_gallon = float(miles_per_gallon)

liters_per_hundred_kilometers = 235.214583 / miles_per_gallon

print("The fuel efficiency in liters-per-hundred-kilometers is", round(liters_per_hundred_kilometers, 2))
