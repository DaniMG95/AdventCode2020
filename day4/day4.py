
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
import re

path = "input.txt"


def get_passport(path):
    file = open(path)
    passports = []
    data = {}
    for line in file:
        line = line.replace("\n", "")
        if line == "":
            passports.append(data)
            data = {}

        else:
            infos = line.split(" ")
            for info in infos:
                key, value = info.split(":")
                data[key] = value
    passports.append(data)
    return passports

def get_sol_1(passports, keys):
    cnt = 0
    for passport in passports:
        if len(set(keys) - set(passport.keys())) == 0:
            cnt += 1
    return cnt

def get_sol2(passports):
    cnt = 0
    for passport in passports:
        if len(set(keys) - set(passport.keys())) == 0:
            if valid_passport(passport):
                cnt += 1
    return cnt

def valid_byr(byr):
    if byr > 2002 or byr < 1920:
        return False
    return True

def valid_iyr(iyr):
    if iyr > 2020 or iyr < 2010:
        return False
    return True

def valid_eyr(eyr):
    if eyr > 2030 or eyr < 2020:
        return False
    return True

def valid_hgt(hgt):
    if "cm" in hgt:
        value = int(hgt.replace("cm",""))
        if value > 193 or value < 150:
            return False
    elif "in" in hgt:
        value = int(hgt.replace("in",""))
        if value > 76 or value < 59:
            return False
    else:
        return False
    return True

def valid_hcl(hcl):
    if not "#" in hcl:
        return False
    if len(hcl.split("#")[1]) == 6 and len(re.findall("[g-z]",hcl)) ==0:
        return True
    return False

def valid_ecl(ecl):
    keys = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in keys

def valid_pid(pid):
    return len(pid) == 9 and len(re.findall("[0-9]",pid)) == 9


def valid_passport(passport):
    keys = ["byr", "iyr", "eyr"]

    for key in keys:
        if len(passport[key]) != 4:
            return False

    byr = valid_byr(int(passport["byr"]))
    iyr = valid_iyr(int(passport["iyr"]))
    eyr = valid_eyr(int(passport["eyr"]))
    hgt = valid_hgt(passport["hgt"])
    hcl = valid_hcl(passport["hcl"])
    ecl = valid_ecl(passport["ecl"])
    pid = valid_pid(passport["pid"])
    return all([byr, iyr, eyr, hgt, hcl, ecl, pid])




passports = get_passport("input.txt")
print(get_sol_1(passports, keys))
print(get_sol2(passports))