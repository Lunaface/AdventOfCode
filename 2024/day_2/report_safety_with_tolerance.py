reports = [list(map(int,l.split())) for l in open("input.txt").readlines()]

def is_safe(report):
    ascending = report[0] < report[1]

    for i in range(len(report) - 1):
        curr = report[i]
        next = report[i + 1]
        diff = abs(curr - next)

        if (diff < 1 or diff > 3 or 
            ((ascending and curr > next) or (not ascending and curr < next))):
            return False
    return True

result = 0

for report in reports:
    if (is_safe(report)):
        result += 1
    else:
        for level in range(len(report)):
            copy = report[:]
            del copy[level]
            if (is_safe(copy)):
                result += 1
                break

print(result)