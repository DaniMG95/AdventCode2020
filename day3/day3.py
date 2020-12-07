


def get_map(path):
    file = open(path)
    list = []
    for line in file:
        list.append(line.replace("\n",""))
    file.close()
    return list

def dow_map(down, right, map):
    count = 0
    position = [0, 0]
    while position[1]+down < len(map):
        position[0] = (position[0] + right) % len(map[0])
        position[1] += down

        if map[position[1]][position[0]] == "#":
            count += 1
    return count

def result_2(map):
    changes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    total = 1
    for right, down in changes:
        total = total * dow_map(down, right, map)
    return total

map = get_map("input.txt")
print(dow_map(1, 3, map))   #159
print(result_2(map))