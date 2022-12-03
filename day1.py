f = open('/Users/admin/Documents/CodeProjects/nisseMat.txt', 'r')

backpack = f.readlines()
elfBackPack= 0
allBackPack = []
topThree = 0
for stuff in backpack:
    if stuff == "\n":
        allBackPack.append(elfBackPack)
        elfBackPack = 0
    else:
        elfBackPack += int(stuff)
print(max(allBackPack))
topThree = max(allBackPack)
allBackPack.remove(max(allBackPack))
topThree += max(allBackPack)
allBackPack.remove(max(allBackPack))
topThree += max(allBackPack)
print(topThree)