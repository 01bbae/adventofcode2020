f = open('day3.txt', 'r')
x = int(input("enter x: "))
y = int(input("enter y: "))
tree=0
ycount=1
for lines in f:
    if ycount%y==0:
        if lines[x] =='#':
            # print("hit tree")
            tree+=1
        x+=3
        x%=31 #end of line calculation
    ycount+=1

print(tree)
f.close()