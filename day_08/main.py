lines = open("./input", "r").readlines()

def traverse(instructions):
    acc = 0
    i = 0
    visited = list()
    while True:
        if i in visited:
            return acc
        if i >= len(instructions):
            print(f"terminated: acc = {acc}")
            return acc
        visited.append(i)
        op, val = instructions[i].split(" ")
        if op == "jmp":
            i += int(val)
        elif op == "acc":
            acc += int(val)
            i += 1
        elif op == "nop":
            i += 1

# Part 1
print(traverse(lines))

# Part 2
for i in range(len(lines)):
    new = lines.copy()
    if new[i].split(" ")[0] == "jmp":
        new[i] = "nop " + new[i].split(" ")[1]
    elif new[i].split(" ")[0] == "nop":
        new[i] = "jmp " + new[i].split(" ")[1]
    traverse(new)
