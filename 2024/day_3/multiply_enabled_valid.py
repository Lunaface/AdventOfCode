import re

program = open("input.txt").read()
instructions = ["".join(x) for x in re.findall("(mul\(-?[0-9]+,-?[0-9]+\))|(do\(\))|(don't\(\))", program)]

result = 0
enabled = True

for instruction in instructions:
    if (instruction == 'do()'):
        enabled = True
    elif (instruction == 'don\'t()'):
        enabled = False
    else:
        if (enabled):
            sep = instruction.strip('mul(').strip(')').split(',')
            result += int(sep[0]) * int(sep[1])
    
print(result)