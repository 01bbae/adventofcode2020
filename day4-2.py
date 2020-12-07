import re
f = open('day4.txt', 'r')

properties = {'byr', 'iyr','eyr', 'hgt','hcl', 'ecl', 'pid'}
eclprop = {'amb','blu','brn','gry','grn','hzl','oth'}
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
            if 1920 <= int(dict.get('byr')) <= 2002:
                print('passed byr')
                if 2010 <= int(dict.get('iyr')) <= 2020:
                    print('passed iyr')
                    if 2020 <= int(dict.get('eyr')) <= 2030:
                        print('passed eyr')
                        if ((dict.get('hgt')[-2:] == 'cm' and 150 <= int(dict.get('hgt')[:-2]) <= 193) or (dict.get('hgt')[-2:] == 'in' and 59 <= int(dict.get('hgt')[:-2]) <= 76)):
                            print('passed hgt')
                            if re.search('#[0-9a-f]{6}', dict.get('hcl')):
                                print('passed hcl')
                                if dict.get('ecl') in eclprop:
                                    print('passed ecl')
                                    if re.search('\d{9}', dict.get('pid')):
                                        print('passed pid')
                                        print('all correct')
                                        print(dict)
                                        valid+=1
        dict.clear() #reset dictionary
if properties.issubset(dict.keys()):
    if 1920 <= int(dict.get('byr')) <= 2002:
                if 2010 <= int(dict.get('iyr')) <= 2020:
                    if 2020 <= int(dict.get('eyr')) <= 2030:
                        if ((dict.get('hgt')[-2:] == 'cm' and 150 <= int(dict.get('hgt')[:-2]) <= 193) or (dict.get('hgt')[-2:] == 'in' and 59 <= int(dict.get('hgt')[:-2]) <= 76)):
                            if re.search('#[0-9a-f]{6}', dict.get('hcl')):
                                if dict.get('ecl') in eclprop:
                                    if re.search('/d{9}', dict.get('pid')):
                                        print('all correct')
                                        print(dict)
                                        valid+=1
        
print(valid)
