grid = { (x, y): char
        for y, row in enumerate (open('input.txt').readlines())
        for x, char in enumerate(row.strip())}
max_x, my_y = max(grid.keys())
directions = [(-1,0),(0,1),(1,0),(0,-1)]

def add_coords(a, b):
    return (a[0] + b[0], a[1] + b[1])

def find_region(start):
    region, area, perimeter = set(), 0, 0
    queue = [start]

    while queue:
        pos = queue.pop()
        if pos in region:
            continue
        region.add(pos)
        area += 1
        for direction in directions:
            new = add_coords(pos, direction)

            if grid.get(new) == grid[pos]:
                queue.append(new)
            else:
                perimeter += 1
    return area, perimeter, region

seen = set()
result = 0
for coord in grid:
    if coord not in seen:
        area, perimeter, region = find_region(coord)
        seen.update(region)
        result += area * perimeter
print(result)