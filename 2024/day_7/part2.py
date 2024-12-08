input = open("input.txt").read().split('\n')

def concatenate(a, b): return int(f"{a}{b}")
def pow_ten(a): return len(str(a))

def valid_equation(final, values):
    if len(values) == 1:
        return values[0] == final
    
    end = values[-1]

    if final % end == 0:
        mul = valid_equation(final / end, values[:-1])
        
        if (mul):
            return mul
        
    pwt = 1
    while pwt <= end:
        pwt *= 10
    if (final - end) % pwt == 0:
        concat = valid_equation((final - end) // pwt, values[:-1])

        if (concat):
            return concat

    return valid_equation(final - end, values[:-1])

result = 0

for equation in input:
    final, values = equation.split(': ')
    final = int(final)
    values = [int(x) for x in values.split(' ')]
    if (valid_equation(final, values)):
        result += final
    
print(result)