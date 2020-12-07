f = open('day5.txt', 'r')

max=0
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
    if max<seatID:
        max = seatID
print(max)