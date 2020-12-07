
file = open("day1/input.txt")

nums = []

def get_2020(nums):
    for num1 in nums:
        for num2 in nums:
            if num1 + num2 == 2020 and num1 != num2:
                return num1 * num2

def get_2020_v2(nums):
    for num1 in nums:
        for num2 in nums:
            for num3 in nums:
                if num1 + num2 + num3 == 2020 and num1 != num2 and num1 != num3 and num2 != num3:
                    return num1 * num2 * num3

for line in file:
    nums.append(int(line))

print(get_2020(nums))
print(get_2020_v2(nums))