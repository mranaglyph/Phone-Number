# Author : mranaglyph
# Date : 05/18/2021

import re # import regular expression module

numbers = [] # phone number tuple/list to populate with valid search results
textClrGrn = '\033[32m' # assigning green text variable with ANSI
textClrRed = '\033[31m' # assigning red text variable with ANSI
textClrYlw = '\033[33m' # assigning yellow text variable with ANSI
default = '\033[m' # assigning default text color with ANSI

# USER SUPPLIES TEXT TO SEARCH IN : 'Read_File.txt' [500MB max file read length]
# user enters where the numbers are from as well to further organize ouput and write file
request = input('\nWhere are these Phone Numbers from? : ')
file = open('Read_File.txt', 'r')
text = file.readlines(500000000)
text = ''.join(text)

# [xxx-xxx-xxxx, (xxx) xxx-xxxx, xxx.xxx.xxxx, xxx xxx xxxx] ---> types of phone number patterns to look for
# 'regex' is a regular expression object, these regex objects are separated out into 4 types to keep all duplicates together, making them easier
# to remove later, since they are only one element apart in the final list this way
# I know phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}|\(\d{3}\)\s\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\d{3}\s\d{3}\s\d{4}') is valid, I didn't want it
# splitting the objects up gives me more control, and gives the user more information/feedback per step, plus it's easier to read IMO
phoneNumRegex1 = re.compile(r'\d{3}-\d{3}-\d{4}')
phoneNumRegex2 = re.compile(r'\(\d{3}\)\s\d{3}-\d{4}')
phoneNumRegex3 = re.compile(r'\d{3}\.\d{3}\.\d{4}')
phoneNumRegex4 = re.compile(r'\d{3}\s\d{3}\s\d{4}')

# check for matches before adding to tuple, or print 'else' if no match (prevents tuple w/blank entries, and nests duplicates)
while True:
    try:
        match1 = re.search(phoneNumRegex1, text)
        if match1:
            numbers.append(phoneNumRegex1.findall(text))
            print(textClrGrn, '\nPhone Number(s) Found! [xxx-xxx-xxxx]')
        else:
            print(textClrRed, '\nNo Phone Number(s) of Format [xxx-xxx-xxxx] Found.')

        match2 = re.search(phoneNumRegex2, text)
        if match2:
            numbers.append(phoneNumRegex2.findall(text))
            print(textClrGrn, '\nPhone Number(s) Found! [(xxx) xxx-xxxx]')
        else:
            print(textClrRed, '\nNo Phone Number(s) of Format [(xxx) xxx-xxxx] Found.')

        match3 = re.search(phoneNumRegex3, text)
        if match3:
            numbers.append(phoneNumRegex3.findall(text))
            print(textClrGrn, '\nPhone Number(s) Found! [xxx.xxx.xxxx]')
        else:
            print(textClrRed, '\nNo Phone Number(s) of Format [xxx.xxx.xxxx] Found.')

        match4 = re.search(phoneNumRegex4, text)
        if match4:
            numbers.append(phoneNumRegex4.findall(text))
            print(textClrGrn, '\nPhone Number(s) Found! [xxx xxx xxxx]')
        else:
            print(textClrRed, '\nNo Phone Number(s) of Format [xxx xxx xxxx] Found.')
    except TypeError:
        print(default, '\n- Search End -')
    break

# converts tuple to list so duplicates can be removed in following try/except for loop
# this needs to be converted since tuples are immutable and don't have any *.pop/*.remove methods :(
# also I tried to enumerate over the tuple, but that did not work either, so conversion from nested tuple 
# to a flat list seemed like the only way to remove duplicates
numbers = list(sum(numbers, []))

# for loop checks each element in list to next element, to validate if they are equal
# if a duplicate is found, it is removed from the list, and when the for loop hits an IndexError
# (when it reaches the end of the numbers list), it prints out all numbers found in list (minus duplicates)
# finally, it writes the numbers list to the 'Write_File.txt' document and closes both the read/write files
for n in range(len(numbers)):
    try:
        if numbers[n] == numbers[n + 1]:
            numbers.remove(numbers[n])
            print(textClrRed, '\nDuplicate Found.')
        else:
            print(textClrGrn, '\nNo Duplicate Found.')
    except IndexError:
        print(textClrYlw, '\nPhone Number(s) List [{}] : \n{}'.format(request, numbers) + '\n', default)
        file.close()
        file2 = open('Write_File.txt', 'a')
        file2.write('[' + str(request) + ']' + '\n' + str(numbers) + '\n\n')
        file2.close()

close = input(':: Press Enter to Close :: \n\n')
if close == True:
    print()
    exit()
else:
    print()
    exit()