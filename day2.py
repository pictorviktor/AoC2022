f = open('/Users/admin/Documents/CodeProjects/strategy.txt', 'r')
strat = f.read()
strat = strat.split('\n')
points = 0
# def part1():
#     for round in strat:
#         if round == 'A X':
#             points += 4 # rock vs rock = 3+1
#         elif round == 'A Y':
#             points += 8 # rock vs paper = 6+2
#         elif round == 'A Z':
#             points += 3 # rock vs scissor = 0+3
#         elif round == 'B X':
#             points += 1 # paper vs rock = 0+1
#         elif round == 'B Y':
#             points += 5 # paper vs paper = 3+2
#         elif round == 'B Z':
#             points += 9 # paper vs scissor = 6+3
#         elif round == 'C X':
#             points += 7 # scissor vs rock = 6+1
#         elif round == 'C Y':
#             points += 2 # scissor vs paper = 0+2
#         elif round == 'C Z':
#             points += 6 # scissor vs scissor = 3+3
                
#     print(points)
# def part2():
for round in strat:
    if round == 'A X':
        points += 3
    elif round == 'A Y':
        points += 4 
    elif round == 'A Z':
        points += 8 
    elif round == 'B X':
        points += 1 
    elif round == 'B Y':
        points += 5 
    elif round == 'B Z':
        points += 9 
    elif round == 'C X':
        points += 2 
    elif round == 'C Y':
        points += 6 
    elif round == 'C Z':
        points += 7 
                
print(points)