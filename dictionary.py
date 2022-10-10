# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:26:43 2022

@author: Vincent Medrano
"""

# For this exercise, write a dictionary that catalogs
# the classes you took last term - the keys should be the
# class CRN number (without the 'CRN' part), and the values
# should be the title of the class.
# Then, write a function 'add class' that takes 2 arguments
# - a class number and a description - and adds the class to your dictionary.
# Use this function to add the classes you’re taking this term to the dictionary.
# Finally, write a function print classes that takes one argument
# - a Course CRN number  - and prints out all the classes you
# took in that have that CRN or a smaller CRN.
# Example output:
# >> print_classes(’77693’)
# Introduction to Python 

# if you input a CRN that is not in your dictionary, say 
# >> print_classes(’99999’) The print the message:
# No Course 99999 classes taken.
# For this exercise,  the key can be a number and the values a string.
# Be sure to test with Course numbers that you both did, and did not take!

# Quick Reference D = {} creates an empty dictionary
# D = {key1:value1, ...} creates a non-empty dictionary
# D[key] returns the value thats mapped to by key. (What if there’s no such key?)
# D[key] = newvalue maps newvalue to key. Overwrites any previous value. Remember - newvalue can be any valid Python data structure.
# del D[key] deletes the mapping with that key from D.
# len(D) returns the number of entries (mappings) in D.
# x in D, x not in D checks whether the key x is in the dictionary D.
# D.keys() - returns a list of all the keys in the dictionary.
# D.values() - returns a list of all the values in the dictionary.

def add_class(key, value):
    if key < 70000 or key > 79999:
        print("You entered a bad CRN, nothing added!\n")
    else:
        class_dict[key] = value
    print("Current dictionary is: \n" ,class_dict)

# current dictionary
class_dict = {78625: "Introduction to Computers and Digital Tech",
              78224: "Data Structures",
              78231: "Introduction to C Programming",}
print("Current classes in dictionary \n", class_dict)

key = int(input("Enter new CRN\n"))  
value = input("Enter the title of the class\n")

add_class(key, value)
