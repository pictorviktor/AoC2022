f = open('/Users/admin/Documents/CodeProjects/AoC2022/AoC2022/inputDay6.txt', 'r')
assignments = f.readlines()
signals = list(assignments[0])

for i in range(len(signals)):
    diff_chars = signals[i:i+14]
    signals[::-1]
   
    if (len(set(diff_chars)) == len(diff_chars)):
        print(i+14)
        break 
 
   
        