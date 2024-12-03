import re

program = open("input.txt").read()
validMuls = re.findall("mul\(-?[0-9]+,-?[0-9]+\)", program)

result = 0

for mul in validMuls:
    sep = mul.strip('mul(').strip(')').split(',')
    result += int(sep[0]) * int(sep[1])
print(result)