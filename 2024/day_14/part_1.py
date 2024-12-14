import re

gridWidth, gridHeight = 101, 103
t = 100
quadrantTL, quadrantTR, quadrantBL, quadrantBR = 0,0,0,0

coordPattern = r"[pv]=(-?\d+),(-?\d+)"
for l in open('input.txt').readlines():
    (posX, posY), (vX, vY) = re.findall(coordPattern, l)
    finalPosX = (int(posX) + t * int(vX)) % gridWidth
    finalPosY = (int(posY) + t * int(vY)) % gridHeight
    
    if finalPosX == gridWidth // 2 or finalPosY == gridHeight // 2:
        continue
    if finalPosX < gridWidth//2 and finalPosY < gridHeight//2:
        quadrantTL += 1
    elif finalPosX > gridWidth//2 and finalPosY < gridHeight//2:
        quadrantTR += 1
    elif finalPosX < gridWidth//2 and finalPosY > gridHeight//2:
        quadrantBL += 1
    else:
        quadrantBR += 1

print(quadrantTL * quadrantTR * quadrantBL * quadrantBR)