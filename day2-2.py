import re
f = open('day2.txt', 'r')
n=0
for line in f:
    ar = line.split()
    num = ar[0].split('-')
    numbers = list(map(int,num))
    char = ar[1].strip(':')
    one = numbers[0]
    two = numbers[1]
    pattern = "^.{" + str(one-1) + "}" + char + ".{"+  str(two-one-1) + "}[^"+char+"]" + "|^.{" + str(one-1) + "}[^" + char +"].{"+str(two-one-1) + "}"+char #-1 is to offset in regex
    if re.search(pattern,ar[2]):
        n+=1
print(n)