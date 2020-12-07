f = open('day3.txt', 'r')
x=0
tree=0
for lines in f:
    if lines[x] =='#':
        # print("hit tree")
        tree+=1
    x+=3
    x%=31 #end of line calculation
print(tree)
f.close()