import string
f = open('day6.txt', 'r')
alpha = list(string.ascii_lowercase)
total = 0
for line in f:
    if line != '\n':
        for char in line:
            if char in alpha:
                alpha.remove(char)
    else:
        total += 26 - len(alpha)
        alpha = list(string.ascii_lowercase)
total += 26 - len(alpha)
print(total)