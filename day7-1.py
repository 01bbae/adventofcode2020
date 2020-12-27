import re
f = open('day7.txt','r')
dict={}
for line in f:
    l = line.strip('.\n')
    l = re.sub(' \d| bags?','',l)
    bags = re.split(' contain |, ',l)
    if bags[1]!='no other':
        dict[bags[0]] = set(bags[1:])

count = 0
def findbags(color,dict):
    if color == 'shiny gold':
        
    else:
        
    # for x in dict.get(color):
    #     print(x)
    #     if(dict.get(x)!= None):
    #         findbags(x,dict)
    #         dict.pop(x)

findbags('shiny gold',dict)
print(dict.get('shiny gold'))
finallen = len(dict)
print(initlen-finallen-1)

