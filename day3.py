import string
f = open('/Users/admin/Documents/CodeProjects/AoC2022/AoC2022/inputDay3.txt', 'r')
bags = f.read()
bags = bags.split('\n')
compartmentList = []
alphabet = [*list(string.ascii_lowercase), *list(string.ascii_uppercase)]
total = 0
compartmentList = []
for item in bags:
    length = len(item)//2
    first, second = (item[:length], item[length:])
    compartmentList.append([first,second])

#print(compartmentList)

for item in compartmentList:
    first, second = item
    for letter in first:
        if letter in second:
            total += alphabet.index(letter) + 1
            break
#print(total)
#print(bags)
badge = []
badge1 = []
total2 = 0
for i in range(0, len(bags), 3):
    badge.append(bags[i:i+3])
for x in badge:
    badge1.append(list(set(x[0])&set(x[1])&set(x[2])))
    

for letter in badge1:
    for x in letter:
        total2 += alphabet.index(x)+1
print(total2)


