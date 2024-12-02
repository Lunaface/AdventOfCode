lines = open("input.txt")

list1 = []
list2 = []

for line in lines:
    listItems = line.strip().split('   ')
    list1.append(int(listItems[0]))
    list2.append(int(listItems[1]))

list1.sort()
list2.sort()

result = 0

for item1, item2 in zip(list1, list2):
    result += abs(item1 - item2)

print(result)
