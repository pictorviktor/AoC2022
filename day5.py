import re
f = open('/Users/admin/Documents/CodeProjects/AoC2022/AoC2022/inputDay5.txt', 'r')
moves = f.readlines()
counter = 0
moveBox = []

stackList = [['m','j','c','b','f','r','l','h']
,['z','c','d']
,['h','j','f','c','n','g','w']
,['p','j','d','m','p','s','b']
,['n','c','d','r','j']
,['w','l','d','q','p','j','g','z']
,['p','z','t','f','r','h']
,['l','v','m','g']
,['c','b','g','p','f','q','r','j']]


for i in moves:
    moves[counter] = re.split(r"\n|move | from | to ", i)
    moves[counter] = moves[counter][1:4]
    moves
    counter+=1

moves = [[int(x) for x in i] for i in moves]

for move in moves:
    for i in range(move[0]):
        
        moveBox.append(stackList[move[1]-1][-1])
        stackList[move[1]-1].pop()
        stackList[move[2]-1].append(moveBox[0])
        moveBox = []

print(stackList)  

for stack in stackList:
     print(stack[-1])