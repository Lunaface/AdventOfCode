from collections import defaultdict

grid = { (x, y): char
        for y, row in enumerate (open('input.txt').readlines())
        for x, char in enumerate(row.strip('\n'))}
max_x, max_y = max(grid.keys())
delta = -1,0,1

result = sum( "XMAS" == "".join( grid.get( ( x + dx * n, y + dy * n ), "" )
                               for n in range( 4 ) )
            for x in range( max_x + 1 )
            for y in range( max_y + 1 )
            for dx in delta
            for dy in delta )
print(result)