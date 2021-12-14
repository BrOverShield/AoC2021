# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def displayMap(map):
	maxX = 0
	minX = 0
	maxY = 0
	minY = 0
	Xs = []
	Ys = []
	for dot in map:
		x = int(dot.split(",")[0])
		y = int(dot.split(",")[1])
		Xs.append(x)
		Ys.append(y)
	maxX = max(Xs)
	maxY = max(Ys)
	minX = min(Xs)
	minY = min(Ys)

	for y in range(minY, maxY+1):
		line = ""
		for x in range(minX, maxX+1):
			name = str(x) + "," + str(y)
			if name in map:
				line += "#"
			else:
				line += "."
		print(line)

def D13S1():
	map = set()
	path = "2021_D13_Dots.txt"
	with open(path) as file:
		lines = file.readlines()
		lines = [line.strip() for line in lines]

		for line in lines:
			x = int(line.split(",")[0])
			y = int(line.split(",")[1])
			if x > 655:
				x = 655*2 - x
				map.add(str(x) + "," + str(y))
			else:
				map.add(line)
	#displayMap(map)
	print(len(map))

def D13S2():
	map = set()
	newMap = set()
	path = "2021_D13_Dots.txt"
	foldsPath = "2021_D13_Folds.txt"
	with open(path) as file:
		lines = file.readlines()
		lines = [line.strip() for line in lines]
		map.update(lines)
		with open(foldsPath) as foldsFile:
			folds = foldsFile.readlines()
			folds = [fold.strip().replace("fold along ", "") for fold in folds]
			for fold in folds:
				parameter = fold.split("=")[0]
				amount = int(fold.split("=")[1])
				newMap = set()
				for dot in map:
					x = int(dot.split(",")[0])
					y = int(dot.split(",")[1])
					if parameter == "x":
						if x > amount:
							x = amount*2 - x
							newMap.add(str(x) + "," + str(y))
						else:
							newMap.add(dot)
					if parameter == "y":
						if y > amount:
							y = amount*2 - y
							newMap.add(str(x) + "," + str(y))
						else:
							newMap.add(dot)
				map = newMap.copy()
	displayMap(map)
	print(len(map))

D13S2()