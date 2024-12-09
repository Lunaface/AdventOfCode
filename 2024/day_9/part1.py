expanded = []
file = True
id = 0

for c in open('input.txt').readline():
    c = int(c)
    if (file):
        for item in range(c):
            expanded.append(id)
        id += 1
    else:
        for empty in range(c):
            expanded.append('.')
    file = not file

def calculate_checksum(input):
    checksum = 0
    for idx, x in enumerate(input):
        if (x == '.'):
            break
        checksum += x * idx
    return checksum

def move_block_to_empty(input, idx):
    first_empty = input.index('.')

    if (first_empty < idx):
        input[idx], input[first_empty] = input[first_empty], input[idx]
    return first_empty < idx

can_move = True
current_index = len(expanded) - 1
while can_move:
    if expanded[current_index] == '.':
        current_index -= 1
        continue

    can_move = move_block_to_empty(expanded, current_index)
    current_index -= 1

print(calculate_checksum(expanded))
