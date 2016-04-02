# Lesson 2.3: Function

# Read through the code below. Even if you don't understand it, try to make 
# a guess about what it does. What do you think will happen when you press 
# "Test Run"? Once you have a prediction, press "Test Run" and compare what 
# happens to what you predicted.

def say_hello():
    return "Hello!"

print (say_hello())

# say_hello is a function. Or, as Dave would call it, a procedure.
# This procedure isn't particularly interesting because it only does
# one thing. 

# Continue to the next example to see a more interesting version of say_hello.

# Once again, say_hello is a function (AKA procedure). But this time, it DOESN'T
# do the same thing every time. 
#
# Read through the code and try to predict what the output will be when 
# you press "Test Run"

def say_hello(name): #name is the variable used in the function
    greeting = "Hello " + name + "!"
    return greeting

print (say_hello("Miriam"))
print (say_hello("Andy"))

def say_hello(name):
    greeting = "Hello " + name + '!'
    return greeting
# In the previous example, you saw code that looked like what you see above.
# Look at the first line. In that line, 'name' is a "parameter"
# of the function say_hello

# In the code below, the add_two_numbers function has two parameters.
# What do you think will happen when you press "Test Run"?
# Make a prediction and then press "Test Run"
def add_two_numbers(number_1, number_2):
    return number_1 + number_2

print (add_two_numbers(4, 3))
print (add_two_numbers(2, 6))
print (add_two_numbers(0, 9))

# Once you've pressed Test Run, remove the comment characters from the 
# code below and then make ONE modification so that the function does 
# what the name says it should do.

def subtract_two_numbers(number_1, number_2):
    return number_1 - number_2

print (subtract_two_numbers(4, 3))

#Real lesson start here

# Lesson 2.3: Procedures

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4141089439/m-48667860

def rest_of_string(s):
    return s[1:]

print (rest_of_string('audacity'))

# Add your own code and notes here

# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

def udacify(s) :
    return 'U' + s

print (udacify('dacians'))

# the output should be the string 'Udacians'

# Remove the hash, #, from infront of print to test your code.

print (udacify('dacians'))
#>>> Udacians

print (udacify('turn'))
#>>> Uturn

print (udacify('boat'))
#>>> Uboat
