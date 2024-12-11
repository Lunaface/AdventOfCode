stones = [int(x) for x in open('input.txt').readline().split()]
known_evaluations = {}

def split(value):
    str_val = str(value)
    mid = len(str_val) // 2
    return [int(str_val[:mid]), int(str_val[mid:])]

def handle_blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        return split(stone)
    else:
        return [stone * 2024]

def blink(stone, steps):
    if (stone, steps) in known_evaluations:
        return known_evaluations[(stone, steps)]
    stones = handle_blink(stone)
    if steps == 1:
        return len(stones)
    result = sum(blink(stone, steps - 1) for stone in stones)
    known_evaluations[(stone, steps)] = result
    return result
    
print(sum(blink(stone, 75) for stone in stones))