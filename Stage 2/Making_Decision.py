# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48727556/m-48724313

print (2 < 3)
print (21 < 3)
print (7 * 3 < 21)
print (7 * 3 != 21)
print (7 * 3 == 21)

# Add your own code and notes here

print ("Example 1: Greater-than and less-than comparisons")
print (2 > 1)
print (1 > 2)
print (5 < 20)
print (100 < 19)


print ("Example 2: Equality and non-equality comparisons")
print (5 == 5)
print ("hello" == "hello")
print (5 == 10)
print (5 == '5') # what do you think will happen here?
print (7 != 10)
print (7 != 7)


print ("Example 3: A demo of what you are about to learn")
if 3 < 5:
    print ("Three is definitely smaller than 5!")

if 10 > 20: 
    print ("Did you know that 10 is greater than 20!?")
else:
    print ("20 is greater than 10")

# Lesson 2.4: While Loops

# Loops are an important concept in computer programming.
# Loops let us run blocks of code many times which can be
# really useful when we have to repeat tasks.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48686708/m-48480488

def count():
    i = 0
    while i < 10:
        print (i)
        i = i + 1

count()

# Add your own code and notes here

# This code demonstrates a while loop with a "counting variable"
i = 0
while i < 10:
    print (i)
    i = i+1

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces
print (remove_spaces("hello my name is andy how are you?"))

#Work Session 4

# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]
        
def process_madlib(mad_lib):
    processed = ""
    while mad_lib != '':
        box = mad_lib[0:4]
        processed = processed + word_transformer(box)
        if box == 'NOUN' or box == 'VERB':
            mad_lib = mad_lib[4:]
        else:
            mad_lib = mad_lib[1:]
    return processed
    
    
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print (process_madlib(test_string_1))
print (process_madlib(test_string_2))
