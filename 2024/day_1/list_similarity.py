lines = open("input.txt")

list1 = []
list2 = []

for line in lines:
    listItems = line.strip().split('   ')
    list1.append(int(listItems[0]))
    list2.append(int(listItems[1]))

result = 0

foundValues = {}

for number in list1:
    if number in foundValues:
        result += foundValues[number]
        continue

    occurrences = list2.count(number)
    score = number * occurrences
    foundValues[number] = score
    result += score


print(result)