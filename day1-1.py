f = open('day1.txt', 'r')
amt = []
for x in f:
    amt.append(int(f.readline().rstrip()))

amt.sort()
front = 0
back = len(amt)-1
while amt[front]+amt[back]!=2020:
    if amt[front]+amt[back]>2020:
        back-=1
    elif amt[front]+amt[back] < 2020:
        front+=1
if front<=back:
    multi = amt[front] * amt[back]
    print(amt[front], " + ", amt[back], " = ")
    print(multi)
else:
    print("error: match found")
f.close()