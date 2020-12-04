import re

inputs = open("./input", "r").readlines()


class Passport:
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

    def print_values(self):
        print(f"byr: {self.byr}")
        print(f"iyr: {self.iyr}")
        print(f"eyr: {self.eyr}")
        print(f"hgt: {self.hgt}")
        print(f"hcl: {self.hcl}")
        print(f"ecl: {self.ecl}")
        print(f"pid: {self.pid}")
        print(f"cid: {self.cid}")
        print("\n")


# generate a list of all passports
passport = Passport()
passports = list()
for line in inputs:
    line = line.strip()
    if line == "":
        passports.append(passport)
        passport = Passport()
    values = [pair.split(":") for pair in line.split(" ")]
    for pair in values:
        if pair[0] == "byr":
            passport.byr = pair[1]
        elif pair[0] == "iyr":
            passport.iyr = pair[1]
        elif pair[0] == "eyr":
            passport.eyr = pair[1]
        elif pair[0] == "hgt":
            passport.hgt = pair[1]
        elif pair[0] == "hcl":
            passport.hcl = pair[1]
        elif pair[0] == "ecl":
            passport.ecl = pair[1]
        elif pair[0] == "pid":
            passport.pid = pair[1]
        elif pair[0] == "cid":
            passport.cid = pair[1]
passports.append(passport)  # append the final passport

count = 0
for passport in passports:
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    if passport.byr:
        byr = bool(int(passport.byr) in range(1920, 2002 + 1))
    if passport.iyr:
        iyr = bool(int(passport.iyr) in range(2010, 2020 + 1))
    if passport.eyr:
        eyr = bool(int(passport.eyr) in range(2020, 2030 + 1))
    if passport.hgt:
        if re.match("^[0-9]+cm$", passport.hgt):
            if int(re.search("^[0-9]+", passport.hgt).group()) in range(150, 193 + 1):
                hgt = True
        elif re.match("^[0-9]+in$", passport.hgt):
            if int(re.search("^[0-9]+", passport.hgt).group()) in range(59, 76 + 1):
                hgt = True
    if passport.hcl:
        hcl = bool(re.match("^#[0-9a-f]{6}$", passport.hcl))
    if passport.ecl:
        ecl = bool(
            passport.ecl == "amb"
            or passport.ecl == "blu"
            or passport.ecl == "brn"
            or passport.ecl == "gry"
            or passport.ecl == "grn"
            or passport.ecl == "hzl"
            or passport.ecl == "oth"
        )
    if passport.pid:
        pid = bool(re.match("^[0-9]{9}$", passport.pid))

    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        count += 1

print(count)
