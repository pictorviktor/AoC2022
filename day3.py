import string
f = open('/Users/admin/Documents/CodeProjects/inputDay3.txt', 'r')
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
print(total)

for item in bags:
    
