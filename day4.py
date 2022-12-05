import re
f = open('/Users/admin/Documents/CodeProjects/inputDay4.txt', 'r')
assignments = f.readlines()
counter = 0

nr_of_overlapping = 1
less = 0
for i in assignments:
    assignments[counter] = re.split(r"\n|,|-", i)
    counter += 1
for i in assignments:
    del i[-1]
assignments = [[int(x) for x in i] for i in assignments]

for i in assignments:
    
    if len(i) != 4:
        continue
    elif i[0]<=i[2] and i[1]>=i[3]:
        nr_of_overlapping += 1
    elif i[0]>=i[2] and i[1]<=i[3]:
        nr_of_overlapping += 1
    elif i[0]<i[2] and i[1]>=i[2]:
        nr_of_overlapping += 1
    elif i[2]<i[0] and i[3]>=i[0]:
        nr_of_overlapping += 1
    else:
        continue
#print(assignments)
print(nr_of_overlapping)

#print(assignments)