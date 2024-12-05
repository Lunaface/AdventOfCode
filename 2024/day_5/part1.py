input = open('input.txt')

line = input.readline()
rules = {}
result = 0

def has_intersection(list1, list2):
    return bool(set(list1) & set(list2))

def is_valid(update):
    seen = []

    for step in update:
        step = int(step)

        if step in rules:
            if has_intersection(rules[step], seen):
                return False
        seen.append(step)
    return True

while (line != '\n'):
    first, second = line.strip('\n').split('|')
    first = int(first)
    second = int(second)
    if first in rules:
        rules[first].append(second)
    else:
        rules[first] = [second]
    line = input.readline()

for update in input.readlines():
    update = update.strip('\n').split(',')
    if (is_valid(update)):
        result += int(update[len(update)//2])

print(result)