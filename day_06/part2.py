lines = open("./input", "r").readlines()

answers = list()
group = str()
groupsize = 0
for line in lines:
    if line == "\n":
        # casting to set first to remove duplicate letters
        answers.append(str(groupsize) + group)
        group = str()
        groupsize= 0
    else:
        group += line.strip()
        groupsize += 1
answers.append(str(groupsize) + group)

count = 0
for group in answers:
    groupsize = int(group[0])
    for letter in set(group[1:]):
        if group[1:].count(letter) == groupsize:
            count += 1
print(count)
