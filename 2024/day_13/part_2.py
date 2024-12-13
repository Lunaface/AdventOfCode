import re

class Machine:
    costA, costB = 3, 1
    buttonCap = 100
    dA, dB = (0, 0), (0, 0)
    prizeLocation = (0, 0)

    def __init__(self, deltaA, deltaB, prizeCoords):
        self.dA, self.dB = deltaA, deltaB
        pX, pY = prizeCoords
        self.prizeLocation = (pX + 10000000000000, pY + 10000000000000)

    def cheapest_path(self):
        ax, ay = self.dA
        bx, by = self.dB
        px, py = self.prizeLocation

        determinant = ax * by - bx * ay

        if determinant == 0:
            return 0
        
        adiff = by * px - bx * py
        bdiff = ax * py - ay * px

        if adiff % determinant != 0 or bdiff % determinant != 0:
            return 0
        
        a_count = adiff // determinant
        b_count = bdiff // determinant

        if a_count < 0 or b_count < 0: 
            return 0

        return self.costA * a_count + self.costB * b_count



machines = []

coordPattern = r"[XY][+=-](\d+)"
for machine_def in open('input.txt').read().split('\n\n'):
    coords = re.findall(coordPattern, machine_def)
    machines.append(Machine((int(coords[0]), int(coords[1])), (int(coords[2]), int(coords[3])), 
                            (int(coords[4]), int(coords[5]))))


result = 0

for machine in machines:
    cheapest = machine.cheapest_path()
    result += cheapest
print(result)