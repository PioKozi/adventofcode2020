lines = open("./input", "r").readlines()

answers = list()
group = str()
for line in lines:
    if line == "\n":
        # casting to set first to remove duplicate letters
        answers.append("".join(set(group)))
        group = str()
    else:
        group += line.strip()
answers.append("".join(set(group)))

count = int()
for i in answers:
    count += len(i)
print(count)
