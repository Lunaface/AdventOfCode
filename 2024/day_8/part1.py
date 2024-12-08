antinodes = set()

grid = { (x, y): char
        for y, row in enumerate (open('input.txt').readlines())
        for x, char in enumerate(row.strip('\n'))}
max_x, max_y = max(grid.keys())

antennas = {}

for x in range(max_x + 1):
    for y in range(max_y + 1):
        antenna = grid[(x, y)]
        if antenna != ".":
            if antenna in antennas:
                antennas[antenna].append((x, y))
            else:
                antennas[antenna] = [(x, y)]

def find_antinode(antenna1, antenna2):
    x1, y1 = antenna1
    x2, y2 = antenna2

    anti_x = x2 + (x2 - x1)
    anti_y = y2 + (y2 - y1)

    # Only add if in bounds
    if anti_x >= 0 and anti_x <= max_x and anti_y >= 0 and anti_y <= max_y:
        antinodes.add((anti_x, anti_y))

def find_antinodes(antenna1, antenna2):
    find_antinode(antenna1, antenna2)
    find_antinode(antenna2, antenna1)

for antenna in antennas:
    positions = antennas[antenna]
    # loop over every antenna position and find the antinodes
    for i in range(len(positions)):
        for j in range(i):
            find_antinodes(positions[i], positions[j])

print(len(antinodes))