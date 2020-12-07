name = "input.txt"

def count_key(name):
    file = open(name)
    count = 0
    for line in file :
        limit, key = line.split(":")
        limit_1 = int(limit.split("-")[0])
        limit_2 = int(limit.split("-")[1].split(" ")[0])
        limit_key = limit.split("-")[1].split(" ")[1]
        key = key.replace(" ","")
        num = key.count(limit_key)
        if num >= limit_1 and num <= limit_2:
            count = count + 1
    return count


def count_key_v2(name):
    file = open(name)
    count = 0
    for line in file :
        limit, key = line.split(":")
        limit_1 = int(limit.split("-")[0])
        limit_2 = int(limit.split("-")[1].split(" ")[0])
        limit_key = limit.split("-")[1].split(" ")[1]
        key = key.replace(" ","")
        if (key[limit_1-1] == limit_key and not key[limit_2-1] == limit_key) or (not key[limit_1-1] == limit_key and key[limit_2-1] == limit_key):
            count = count + 1
    file.close()
    return count

print(count_key(name))
print(count_key_v2(name))