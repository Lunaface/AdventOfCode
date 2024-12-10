from queue import Queue

grid = { (x, y): int(char)
        for y, row in enumerate (open('input.txt').readlines())
        for x, char in enumerate(row.strip())}
max_x, max_y = max(grid.keys())
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def find_paths(coords):
    queue = Queue()
    queue.put(coords)
    paths = 0
    visited = {coords}

    while not queue.empty():
        curr = queue.get()

        for direction in directions:
            nx, ny = curr[0] + direction[0], curr[1] + direction[1]
            if (nx >= 0 and nx <= max_x and ny >= 0 and ny <= max_y):
                next = (nx, ny)

                if next not in visited and grid[next] - grid[curr] == 1:
                    visited.add(next)
                    if grid[next]==9:
                        paths += 1
                    else:
                        queue.put(next)

    return paths

start_coords = [coord for coord in grid if grid[coord] == 0]
result = 0

for start_coord in start_coords:
    result += find_paths(start_coord)

print(result) 