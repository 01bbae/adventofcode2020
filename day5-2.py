f = open('day5.txt', 'r')

list=[]

for lines in f:
    # f = 0
    # b = 1
    binary1=''
    binary2=''
    for x in range(7):
        if lines[x] == 'F':
            binary1 += '0'
        else:
            binary1 += '1'

    for x in range(7,10):
        if lines[x] == 'L':
            binary2 += '0'
        else:
            binary2 += '1'
    row =int(binary1,2)
    column = int(binary2,2)
    seatID = row*8+column
    list.append(seatID)
list.sort()
for n in range(len(list)-2):
    if list[n]+2==list[n+1]:
        print('found: ', list[n]+1)