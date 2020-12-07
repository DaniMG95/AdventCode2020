import math




def get_id(key):
    row1 = 0
    row2 = 127
    col1 = 0
    col2 = 7

    for letter in key:
        if letter == "F":
            row2 -= math.ceil((row2 - row1) / 2)
        elif letter == "B":
            row1 += math.ceil((row2 - row1) / 2)
        elif letter == "R":
            col1 += math.ceil((col2 - col1) / 2)
        elif letter == "L":
            col2 -= math.ceil((col2 - col1) / 2)
    return row1 * 8 + col1

def get_sol1(path):
    seats = []
    file = open(path)
    for line in file:
        seats.append(get_id(line))
    return seats

def get_sol2(seats):
    for i in range(9, 127*8):
        if i not in seats:
            return i


seats = get_sol1("input.txt")
print(max(seats)) #813
print(get_sol2(seats))