# Lesson 2.1: Introduction to Serious Programming

# Programming is grounded in arithmetic, so it's important
# to know how programming languages do simple math.
# Thankfully, Python follows the same math rules people do.
# See if you can predict the output of this code.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

print (3)
print (1+1)
print (52*3+12*9)
print ((52*3)+(12*9))
print (52*(3+12)*9)

# Write a Python program that prints out the number of minutes in seven weeks.
# Remember: 7 weeks 7 days in a week, 24 hours in a day, and 60 mins in an hour.
# Multiplying these numbers together will give you the result

print (7*7*24*60)

# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the values
# defined below.    
speed_of_light = 299792458   #meters per second
centimeters = 100            #one meter is 100 centimeters
nanosecond = 1.0/1000000000  #one billionth of a second

print (speed_of_light*centimeters*nanosecond)
