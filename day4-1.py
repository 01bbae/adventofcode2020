import re
f = open('day4.txt', 'r')

valid=0


for lines in f:
    if lines!='\n':
        list = re.split('.[3]:|\s',lines) # creates an emtpy list item at the end because newline is a \s character so delete
        print(list) #problem in the last line with no return also not spliting the way I want
        




