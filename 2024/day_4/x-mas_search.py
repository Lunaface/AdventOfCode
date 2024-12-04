from collections import defaultdict

grid = { (x, y): char
        for y, row in enumerate (open('input.txt').readlines())
        for x, char in enumerate(row.strip('\n'))}
max_x, max_y = max(grid.keys())
delta = -1,0,1

search = ["MAS", "SAM"]

result = sum( "".join( [ 
                        # Top left
                        grid.get( ( x - 1, y - 1 ), "" ),
                        # middle
                        grid.get( ( x, y ), "" ),
                        # bottom right
                        grid.get( ( x + 1, y + 1 ), "" ) ] ) in search and
              "".join( [
                        # Top right 
                        grid.get( ( x - 1, y + 1 ), "" ),
                        # middle
                        grid.get( ( x, y ), "" ),
                        # bottom left
                        grid.get( ( x + 1, y - 1 ), "" ) ] ) in search
            for x in range( max_x + 1 )
            for y in range( max_y + 1 ) ) 
print(result)