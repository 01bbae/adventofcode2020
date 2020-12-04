import re
f = open('day2.txt', 'r')
n=0
for line in f:
    ar = line.split()
    num = ar[0].split('-')
    # print(num)
    char = ar[1].strip(':')
    # pattern = '['+ char +']' + '{'+num[0]+','+num[1]+'}'
    numbers = list(map(int,num))
    # print(pattern)
    # if re.search(pattern,ar[2]):
    #     n+=1
    #     print(ar[2])
    occur=0
    for c in ar[2]:
        if c==char:
            occur+=1
    if numbers[0] <= occur <= numbers[1]:
        n+=1
        # print(ar[2])
print("matching passwords: ", n)

# no regex combination possible?