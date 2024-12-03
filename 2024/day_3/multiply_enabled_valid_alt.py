import re

program = open("input.txt").read()
instructions = re.findall("(do\(\))|(don't\(\))|(mul\((-?[0-9]+),(-?[0-9]+)\))", program)

result = 0
enabled = True

for do, dont, _, a, b in instructions:
    if (do or dont):
        enabled = bool(do)
    elif (enabled):
        result += int(a) * int(b)
        
print(result)