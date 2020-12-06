lines = open("./input", "r").readlines()

# Part 1
ids = list()
for line in lines:
    rows = [i for i in range(128)]
    cols = [i for i in range(8)]
    for letter in line[:7]:
        if letter == 'F':
            rows = rows[:len(rows)//2]
        elif letter == 'B':
            rows = rows[len(rows)//2:]
    for letter in line[7:]:
        if letter == 'L':
            cols = cols[:len(cols)//2]
        if letter == 'R':
            cols = cols[len(cols)//2:]
    row = rows[0]
    col = cols[0]
    ids.append(row * 8 + col)
print(f"{max(ids)}")

# Part 2
all_ids = [i for i in range(min(ids), max(ids)+1)]
for i in all_ids:
    if i not in ids and i+1 in ids and i-1 in ids:
        print(i)
