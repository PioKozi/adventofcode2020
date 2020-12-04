numbers = open("./numbers", "r").readlines()
numbers = [int(i) for i in numbers]

for i in numbers:
    covered = 2020 - i
    for j in numbers:
        if covered - j in numbers:
            print((covered - j) * j * i)
