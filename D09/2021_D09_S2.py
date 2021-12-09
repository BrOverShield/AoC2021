lines = []
analysing = set()
completed = set()

def exploreBranch(x, y):
	name = str(x) + "," + str(y)
	analysing.add(name)
	if y != 0:
		branchName = str(x) + "," + str(y-1)
		if lines[y-1][x] != str(9) and branchName not in completed and branchName not in analysing:
			exploreBranch(x, y-1)
			completed.add(str(x) + "," + str(y-1))
	if y != len(lines)-1:
		branchName = str(x) + "," + str(y+1)
		if lines[y+1][x] != str(9) and branchName not in completed and branchName not in analysing:
			exploreBranch(x, y+1)
			completed.add(str(x) + "," + str(y+1))
	if x != 0:
		branchName = str(x-1) + "," + str(y)
		if lines[y][x-1] != str(9) and branchName not in completed and branchName not in analysing:
			exploreBranch(x-1, y)
			completed.add(str(x-1) + "," + str(y))
	if x != len(lines[0])-1:
		branchName = str(x+1) + "," + str(y)
		if lines[y][x+1] != str(9) and branchName not in completed and branchName not in analysing:
			exploreBranch(x+1, y)
			completed.add(str(x+1) + "," + str(y))
	completed.add(name)

path = "2021_D09.txt"
lowPoints = {}
risk = 0
results = []
with open(path) as file:
	lines = file.read().splitlines()
	for y, line in enumerate(lines):
		for x, number in enumerate(line):
			if y != 0:
				if lines[y-1][x] <= number:
					continue
			if y != len(lines)-1:
				if lines[y+1][x] <= number:
					continue
			if x != 0:
				if lines[y][x-1] <= number:
					continue
			if x != len(line)-1:
				if lines[y][x+1] <= number:
					continue
			lowPoints[str(x) + "," + str(y)] = {str(x) + "," + str(y)}

	for coordinates in list(lowPoints.keys()):
		completed = set()
		analysing = set()
		x = int(coordinates.split(",")[0])
		y = int(coordinates.split(",")[1])
		exploreBranch(x, y)
		results.append(len(completed))
	length = len(results)
	results = sorted(results)
	product = results[length-1] * results[length-2] * results[length-3]
	print(product)