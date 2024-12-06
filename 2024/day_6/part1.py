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
    _path.append(next)
    return (next, direction)

direction = (0, -1)
path = [position]
while is_in_grid(position):
    position, direction = walk(path, position, direction)
print(len(set(path)))