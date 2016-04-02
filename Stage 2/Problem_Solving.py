# Lesson 2.7: How to Solve Problems - Days Between Dates

# In this lesson, you'll be working on solving a much
# bigger problem than those you've seen so far. If you
# want, you can use this starter code to write your
# quiz responses and then copy and paste into the
# Udacity quiz nodes.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4184188665/m-108325398

# Simple Mechanical Algorithm
# days = 0
# while date1 is before date2:
#     date1 = advance to next day
#     days += 1

# Fill in the functions below to solve the problem.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    if isLeapYear(year) and month == 2:
        return 29
    else:   
        return daysOfMonths[month-1]

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
        year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

# Below is a testing script that will check if your code is doing
# what it is supposed to. Don't change it! The test will run
# when you execute the file.
# Bonus: Can you figure out how the test works?

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523),
                  ((2013,1,1,1999,12,31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print ("Test with data:", args, "failed")
            else:
                print ("Test case passed!")
        except AssertionError:
            if answer == "AssertionError":
                print ("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print ("Check your work! Test case {0} should not raise AssertionError!\n".format(args))            
#test()

print (daysBetweenDates(1992,10,27,2016,2,21))