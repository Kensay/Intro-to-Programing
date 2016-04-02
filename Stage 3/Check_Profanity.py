# Lesson 3.3: Use Classes
# Mini-Project: Check Profanity

# Typos can be embarassing! Imagine how you'd feel if you
# accidentally sent your boss an email that said "I'll take
# a sh!t at it" instead of "I'll take a shot at it". Write
# a program that can detect curse words in a string of text.

# Use this space to describe your approach to the problem.
#
#
#
#

import urllib.request as ur

def read_text():
    # Your code here.
    quotes = open(r"C:\Users\Jonathan\Documents\GitHub\Udacity\Stage 3\movie_quotes.txt") #Need to use Raw string to make it work
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text):
    # Your code here.
    connection = ur.urlopen("http://www.wdyl.com/profanity?q="+text)
    output = connection.read()
    print(output)
    connection.close

read_text()