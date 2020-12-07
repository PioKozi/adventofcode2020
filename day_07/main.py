import re

inputfile = open("./input", "r")

contained_by = dict()
must_contain = dict()

# make the map which maps a colour to what it can contain
for line in inputfile:
    line = line.strip()
    relevant_bags = list()
    parts = line.split("contain")
    parts += parts.pop(1).split(",")
    parts = [part.replace("bags", "").replace("bag", "").strip(" .") for part in parts]
    contained_by[parts[0]] = [i for i in parts[1:] if i != "no other"]

# make the map which maps colour to what it can be contained by (reverse of above)
for i in contained_by:
    i = re.sub("\d+ ", "", i)
    must_contain[i] = list()
for i in contained_by:
    i = re.sub("\d+ ", "", i)
    for j in contained_by[i]:
        j = re.sub("\d+ ", "", j)
        must_contain[j].append(i)

# Part 1
possible = set()
def traverse(possible, current):
    for i in must_contain[current]:
        possible.add(i)
        traverse(possible, i)
    return possible
possible = traverse(possible, "shiny gold")
print(len(possible))

# Part 2
required = 0
def traverse(required, current):
    for i in contained_by[current]:
        required += int(re.search("\d+", i).group())
        for j in range(int(re.search("\d+", i).group())): # per required bag
            required = traverse(required, re.sub("\d+ ", "", i))
    return required
required = traverse(required, "shiny gold")
print(required)
