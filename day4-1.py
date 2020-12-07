import re
f = open('day4.txt', 'r')

properties = {'byr', 'iyr','eyr', 'hgt','hcl', 'ecl', 'pid'}
valid=0

dict={}

for lines in f:
    if lines!='\n':
        list = re.split(r'[: \n]',lines) # creates an emtpy list item at the end because newline is a \s character so delete
        # print(list) #problem in the last line with no return also not spliting the way I want
        if list[-1] =='':
            list.pop() #if newline, remove from list
        for e in range(0,len(list)-1,2):
            dict[list[e]] = list[e+1]
        # print(dict)
    else:
        if properties.issubset(dict.keys()):
            print('all correct')
            print(dict)
            valid+=1
        dict.clear() #reset dictionary
if properties.issubset(dict.keys()):
            print('all correct')
            print(dict)
            valid+=1
        
print(valid)
