f = open('day1.txt', 'r')
amt = []
for x in f:
    amt.append(int(f.readline().rstrip()))

amt.sort()

print(amt)
x=1
while 2020-amt[0]-amt[x]>0 and x<len(amt):
    x+=1

print(x)
for n in range(x+1):
    print(amt[n])

for a in range(x):
    for b in range(a+1,x+1):
        if a!=b and 2020-amt[a]-amt[b]>0:
            # for c in range(x,len(amt)):
            #     print(amt[a]," ", amt[b]," ", 2020-amt[a]-amt[b])
            #     if amt[c]==2020-amt[a]-amt[b]:
            #         print("found")
            print(amt[a]," ", amt[b]," ", 2020-amt[a]-amt[b])
            for c in range(len(amt)):
                if amt[c]==2020-amt[a]-amt[b]:
                    print("found")





f.close()