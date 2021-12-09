path = "2021_D09.txt"
lowPoints = {}
risk = 0
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
			lowPoints[str(x) + "," + str(y)] = number
			print(str(x) + "," + str(y))
			risk = risk + int(number) + 1
print(risk)