stones = [int(x) for x in open('input.txt').readline().split()]

def flatten(l):
    flattened = []

    for element in l:
        if isinstance(element, list):
            flattened.extend(element)
        else:
            flattened.append(element)
    return flattened

def split(value):
    str_val = str(value)
    mid = len(str_val) // 2
    return [int(str_val[:mid]), int(str_val[mid:])]

def blink():
    global stones
    for idx, stone in enumerate(stones):
        if stone == 0:
            stones[idx] = 1
        elif len(str(stone)) % 2 == 0:
            stones[idx] = split(stone)
        else:
            stones[idx] = stone * 2024
    stones = flatten(stones)

for _ in range(25):
    blink()

print(len(stones))