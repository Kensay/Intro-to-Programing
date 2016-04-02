# Lesson 2.2: Variables

# Programmers use variables to represent values in their code.
# This makes code easier to read by telling others what values
# mean. It also makes code easier to write by cutting down on
# potentially complicated numbers that repeat in our code.

# We sometimes call numbers without a variable "magic numbers"
# It's best to reduce the amount of "magic numbers" in our code

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48660987

speed_of_light = 299792458.0 #meters per second
billionth = 1.0 / 1000000000.0 #nanosecond
nanostick = speed_of_light * billionth * 100
print (nanostick)

# First Quiz

# https://www.udacity.com/course/viewer#!/c-ud000/l-4128968716/e-48480569/m-48665882

# Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle. 

# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

speed_of_light = 299792458.0  #meters per second
cycles_per_second = 2700000000.0 #2.7 GHz

cycle_distance = speed_of_light/cycles_per_second
cycles_per_second = 2800000000.0 #2.8 GHz

print (cycle_distance)

#The value of cycle_distance refers to the current value of the other variables

cycle_distance = speed_of_light/cycles_per_second
print (cycle_distance)

#Fourth Quiz (the other 2 were simple multiple choice question)

# Write python code that defines the variable 
# age to be your age in years, and then prints 
# out the number of days you have been alive.

age = 25
days_in_year = 365

day_alive = age*days_in_year

print (day_alive)