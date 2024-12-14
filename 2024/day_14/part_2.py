import re

gridWidth, gridHeight = 101, 103
bots = []

coordPattern = r"[pv]=(-?\d+),(-?\d+)"
for l in open('input.txt').readlines():
    (posX, posY), (vX, vY) = re.findall(coordPattern, l)
    bots.append([(int(posX), int(posY)), (int(vX), int(vY))])
    
iterations = 0
while True:
    distinct_positions = set([bot[0] for bot in bots])

    if (len(distinct_positions) == len([bot[0] for bot in bots])):
        break

    for idx,bot in enumerate(bots):
        (posx, posy), (vx, vy) = bot
        bots[idx][0] = ((posx + vx) % gridWidth, (posy + vy) % gridHeight)
    iterations += 1

print(iterations)