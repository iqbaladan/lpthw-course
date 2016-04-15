## Variables and Names

# Numbers of cars
cars = 100

# Space in a car
space_in_a_car = 4.0

# Number of drivers available 
drivers = 30

# Number of Passengers who want to carpool today
passengers = 90

# Counting cars not driven
cars_not_driven = cars - drivers

# Assigning car driven to drivers
cars_driven = drivers

# Counting carpool capacity 
carpool_capacity = cars_driven * space_in_a_car

# Counting average passengers per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

