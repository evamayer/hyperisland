#2. In the US, fuel efficiency for vehicles is normally expressed in miles-per-gallon (*MPG*).
# In Canada, fuel efficiency is normally expressed in liters-per-hundred-kilometers *(L/100 km)*.
# Use your research skills to determine how to convert from *MPG* to *L/100 km*.
# Then create a program that reads a value from the user (in American units) and displays the equivalent
# fuel efficiency in Canadian units.

#*You can use Google to research and use both the `input()` command to receive user input
# and the `print()` command to return results to the console or the terminal.*

miles_per_gallon = input("Please enter the fuel efficiency in miles-per-gallon: ")
miles_per_gallon = float(miles_per_gallon)

liters_per_hundred_kilometers = 235.214583 / miles_per_gallon

print("The fuel efficiency in liters-per-hundred-kilometers is", round(liters_per_hundred_kilometers, 2))
