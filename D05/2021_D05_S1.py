import csv

def addToMap(location, map, sum):
	if location in map:
		map[location] += 1
		if map[location] == 2:
			sum += 1
	else:
		map[location] = 1
	return map, sum

Path = "2021_D05.csv"

map = {}
sum = 0
with open(Path) as File:
	lines = list(csv.reader(File))
	for line in lines:
		x1 = int(line[0])
		y1 = int(line[1])
		x2 = int(line[2])
		y2 = int(line[3])
		#Horizontal
		if x1 == x2:
			maximum = max(y1,y2)
			minimum = min(y1,y2)
			for i in range(minimum, maximum+1):
				location = str(x1) + "," + str(i)
				map,sum = addToMap(location, map, sum)
		#Vertical
		elif y1 == y2:
			maximum = max(x1,x2)
			minimum = min(x1,x2)
			for i in range(minimum, maximum+1):
				location = str(i) + "," + str(y1) 
				map,sum = addToMap(location, map, sum)
		else:
			pass
print(sum)

