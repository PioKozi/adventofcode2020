from itertools import permutations

lines = [int(line) for line in open("./input", "r")]

# Part 1
for i in range(25, len(lines)):
    preamble = lines[i-25:i]
    combinations = permutations(preamble, 2)
    if not any([sum(combination)==lines[i] for combination in combinations]):
        break
invalid = lines[i]
index = i
print(invalid)

# Part 2
found = False
for i in range(0, index+2):
    for j in range(i+1, index+2):
        group = lines[i:j]
        if sum(group) == invalid:
            found = True
            break
    if found:
        break
print(group)
print(group[0] + group[-1])
