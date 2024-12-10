from queue import Queue

grid = { (x, y): int(char)
        for y, row in enumerate (open('input.txt').readlines())
        for x, char in enumerate(row.strip())}
max_x, max_y = max(grid.keys())
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def find_rating(start, end):
    queue = Queue()
    queue.put(start)
    rating = 0

    while not queue.empty():
        curr = queue.get()

        for direction in directions:
            nx, ny = curr[0] + direction[0], curr[1] + direction[1]
            if (nx >= 0 and nx <= max_x and ny >= 0 and ny <= max_y):
                next = (nx, ny)

                if grid[next] - grid[curr] == 1:
                    if next == end:
                        rating += 1
                    else:
                        queue.put(next)

    return rating

start_coords = [coord for coord in grid if grid[coord] == 0]
end_coords = [coord for coord in grid if grid[coord] == 9]
result = sum([find_rating(start, end) for end in end_coords for start in start_coords])
print(result) 