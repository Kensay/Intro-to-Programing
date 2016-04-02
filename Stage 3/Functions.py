# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.

import os

def rename_files():
  file_list = os.listdir(r"C:\Users\jbrodeur\Desktop\Prank\prank")
  print (file_list)
  saved_path = os.getcwd()
  print ("Current Working Directory is "+saved_path)
  os.chdir(r"C:\Users\jbrodeur\Desktop\Prank\prank")
  for file_name in file_list:
    print("Old Name - " + file_name)
    print("Old Name - " + file_name.translate(None, "0123456789"))
    os.rename(file_name, file_name.translate(None, "0123456789"))
  os.chdir(saved_path)

rename_files()
