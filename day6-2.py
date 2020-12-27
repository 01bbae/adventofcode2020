#credit to u/wjholden on reddit


import string
f = open('day6.txt', 'r')
input=f.read().strip().split('\n\n')

def ans(input,fcn):
    for group in input:
        yield len(fcn(*(set(s) for s in group)))

input = [line.split() for line in input]

print(sum(ans(input,set.intersection)))
