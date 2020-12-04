# parsing file
lines = open("./passwords", "r").readlines()
lines = [i.split(":") for i in lines]
lines = [[i[0].split(" "), i[1].strip()] for i in lines]
lines = [[i[0][0].split("-"), i[0][1], i[1]] for i in lines]
lines = [[int(i[0][0]), int(i[0][1]), i[1], i[2]] for i in lines]

# Part 1
"""
lines[i][0] = min
lines[i][1] = max
lines[i][2] = letter
lines[i][3] = phrase
"""
count = int()
for group in lines:
    if group[3].count(group[2]) in range(group[0], group[1] + 1):
        count += 1
print(count)

# Part 2
"""
lines[i][0] = 1st position + 1
lines[i][1] = 2nd position + 1
+ 1 because no 0 indexing
lines[i][2] = letter
lines[i][3] = phrase
"""
count = int()
for group in lines:
    # XOR
    if (group[3][group[0] - 1] == group[2]) != (group[3][group[1] - 1] == group[2]):
        count += 1
print(count)
