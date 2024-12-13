import re

class Machine:
    costA, costB = 3, 1
    buttonCap = 100
    dA, dB = (0, 0), (0, 0)
    prizeLocation = (0, 0)

    def __init__(self, deltaA, deltaB, prizeCoords):
        self.dA, self.dB, self.prizeLocation = deltaA, deltaB, prizeCoords

    def cheapest_path(self):
        cheapest_path = 99999999999
        ax, ay = self.dA
        bx, by = self.dB
        px, py = self.prizeLocation

        for a_count in range(min(100, px // ax + 1)):
            for b_count in range(min(100, px // bx + 1)):
                x = a_count * ax + b_count * bx
                y = a_count * ay + b_count * by
                if x == px and y == py:
                    cost = a_count * self.costA + b_count * self.costB
                    if cost < cheapest_path:
                        cheapest_path = cost

        return cheapest_path



machines = []

coordPattern = r"[XY][+=-](\d+)"
for machine_def in open('input.txt').read().split('\n\n'):
    coords = re.findall(coordPattern, machine_def)
    machines.append(Machine((int(coords[0]), int(coords[1])), (int(coords[2]), int(coords[3])), 
                            (int(coords[4]), int(coords[5]))))


result = 0

for machine in machines:
    cheapest = machine.cheapest_path()
    if cheapest != 99999999999:
        result += cheapest
print(result)