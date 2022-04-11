#!/usr/bin/python

#Import libraries
#
import re
import sys
import glob

#-help option
#
protocol = sys.argv[4]

#If -help is on the command line then the following is executed
#
if protocol in ['-help']:

     #Opening and reading the help file and printing its contents
     #
     with open('help.txt', 'r') as f:
          output = f.read()
          print (output)
     sys.exit()

#Printing the filename and line number of the searched word for the first file
#
print("file:", end = ' ')
print(sys.argv[1])

#Argv[4] is the word you are searching for
#
lookup = sys.argv[4]

#Opening the file to find what line the word is in
#
with open(sys.argv[1]) as file:
    for num, line in enumerate(file, 2):
        if lookup in line:
#Formatting the print statement
            #
            print("Line", end = ' ')
            print(num, end = '')
            print(":", end = ' ')
#Printing the word
#
print(line)

#Repeating the same process for the second file
#
print("file:" , end = ' ')
print(sys.argv[2])

#Finding the word
#
with open(sys.argv[2]) as file:

    #Getting the line number
    #
    for num, line in enumerate(file, 1):
        if lookup in line:

            #Printing the line number and word
            #
            print("Line", end = ' ')
            print(num, end = '')
            print(":", end = ' ')
print(line)

#Same process is repeated for the third file
#
print("file:", end = ' ')
print(sys.argv[3])
#Opening the third file and getting the line number of the word
#
with open(sys.argv[3]) as file:
    for num, line in enumerate(file, 1):
        if lookup in line:

#Printing line number and word
#
            print("Line", end = ' ')
            print(num, end = '')
            print(":", end = ' ')

print(line)

#Printing the number of lines matched
#
print("Lines matched = ", end = ' ')
print(num-5)
