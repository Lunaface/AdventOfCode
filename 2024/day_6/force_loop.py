obstacles = set()
for y, line in enumerate(open('input.txt')):
    for x, object in enumerate(line.strip()):
        if object == '#':
            obstacles.add((x, y))
        if object == '^':
            position = (x, y)

width, height = x, y

def is_in_grid(pos):
    x, y = pos
    return x > 0 and y > 0 and x < width and y < height

def turn(dir):
    dX, dY = dir
    return (-dY, dX)

def walk(_path, position, direction):
    next = (position[0] + direction[0], position[1] + direction[1])
    if (next in obstacles):
        return (position, turn(direction))
    _path.append((next, direction))
    return (next, direction)

# construct the guard's path with movement direction
direction = (0, -1)
path = [(position, direction)]
while is_in_grid(position):
    position, direction = walk(path, position, direction)
    
blocked = set([path[0][0]])
result = 0

for i in range(1, len(path)):
    block_pos, _ = path[i]

    # skip positions we already tried
    if block_pos in blocked:
        continue

    obstacles.add(block_pos)
    # place guard right in front of the new obstruction
    position, direction = path[i - 1]

    # record previous path; if we reenter our previous path we will always loop
    visited = set(path[:i - 1])
    while is_in_grid(position):
        # add this position to the visited set so if we return we know we looped
        visited.add((position, direction))
        position, direction = walk([], position, direction)
        if (position, direction) in visited:
            result += 1
            break
    blocked.add(block_pos)
    obstacles.remove(block_pos)

print(result)