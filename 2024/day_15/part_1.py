grid, commands = open('input.txt').read().split('\n\n')

walls = set()
crates = set()

for y, l in enumerate(grid.split()):
    for x, c in enumerate(l):
        if c == '@':
            bot = (x, y)
        elif c == '#':
            walls.add((x, y))
        elif c == 'O':
            crates.add((x, y))

def moveBox(start, direction):
    newPosition = (start[0] + direction[0], start[1] + direction[1])

    if newPosition in walls:
        return False
    if newPosition in crates:
        if not moveBox(newPosition, direction):
            return False
    
    crates.remove(start)
    crates.add(newPosition)
    return True


def move(direction):
    global bot
    newPosition = (bot[0] + direction[0], bot[1] + direction[1])

    if newPosition in walls:
        return
    
    if newPosition in crates:
        if not moveBox(newPosition, direction):
            return
    
    bot = newPosition

for command in commands:
    if command == '>':
        move((1, 0))
    elif command == 'v':
        move((0, 1))
    elif command == '<':
        move((-1, 0))
    elif command == '^':
        move((0, -1))

result = 0

for crate in crates:
    result += crate[0] + 100 * crate[1]

print(result)