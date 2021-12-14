# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def AffectPerimeter(x, y, lines, sum, flashed):
	if y != 0:
		name = str(x) + "," + str(y - 1)
		if lines[y - 1][x] >= 9:
			flashed.add(name)
			lines[y - 1][x] = 0
			sum += 1
			lines, sum, flashed = AffectPerimeter(x, y - 1, lines, sum, flashed)
		elif name not in flashed:
			lines[y - 1][x] = lines[y - 1][x] + 1

	if y != len(lines) - 1:
		name = str(x) + "," + str(y + 1)
		if lines[y + 1][x] >= 9:
			flashed.add(name)
			lines[y + 1][x] = 0
			sum += 1
			lines, sum, flashed = AffectPerimeter(x, y + 1, lines, sum, flashed)
		elif name not in flashed:
			lines[y + 1][x] = lines[y + 1][x] + 1

	if x != 0:
		name = str(x - 1) + "," + str(y)
		if lines[y][x - 1] >= 9:
			flashed.add(name)
			lines[y][x - 1] = 0
			sum += 1
			lines, sum, flashed = AffectPerimeter(x - 1, y, lines, sum, flashed)
		elif name not in flashed:
			lines[y][x - 1] = lines[y][x - 1] + 1

	if x != len(lines[0]) - 1:
		name = str(x + 1) + "," + str(y)
		if lines[y][x + 1] >= 9:
			flashed.add(name)
			lines[y][x + 1] = 0
			sum += 1
			lines, sum, flashed = AffectPerimeter(x + 1, y, lines, sum, flashed)
		elif name not in flashed:
			lines[y][x + 1] = lines[y][x + 1] + 1

	if y != 0 and x != 0:
		name = str(x - 1) + "," + str(y - 1)
		if lines[y - 1][x - 1] >= 9:
			flashed.add(name)
			lines[y - 1][x - 1] = 0
			sum += 1
			lines, sum, flashed = AffectPerimeter(x - 1, y - 1, lines, sum, flashed)
		elif name not in flashed:
			lines[y - 1][x - 1] = lines[y - 1][x - 1] + 1

	if y != 0 and x != len(lines[0]) - 1:
		name = str(x + 1) + "," + str(y - 1)
		if lines[y - 1][x + 1] >= 9:
			flashed.add(name)
			lines[y - 1][x + 1] = 0
			sum += 1
			lines, sum, flashed = AffectPerimeter(x + 1, y - 1, lines, sum, flashed)
		elif name not in flashed:
			lines[y - 1][x + 1] = lines[y - 1][x + 1] + 1

	if y != len(lines) - 1 and x != 0:
		name = str(x - 1) + "," + str(y + 1)
		if lines[y + 1][x - 1] >= 9:
			flashed.add(name)
			lines[y + 1][x - 1] = 0
			sum += 1
			lines, sum, flashed = AffectPerimeter(x - 1, y + 1, lines, sum, flashed)
		elif name not in flashed:
			lines[y + 1][x - 1] = lines[y + 1][x - 1] + 1

	if y != len(lines) - 1 and x != len(lines[0]) - 1:
		name = str(x + 1) + "," + str(y + 1)
		if lines[y + 1][x + 1] >= 9:
			flashed.add(name)
			lines[y + 1][x + 1] = 0
			sum += 1
			lines, sum, flashed = AffectPerimeter(x + 1, y + 1, lines, sum, flashed)
		elif name not in flashed:
			lines[y + 1][x + 1] = lines[y + 1][x + 1] + 1
	return lines, sum, flashed


def D11S1():
	sum = 0
	lines = []
	path = "2021_D11.txt"
	with open(path) as file:
		lines = file.readlines()
		lines = [list(line.strip()) for line in lines]
		for y, line in enumerate(lines):
			for x, number in enumerate(line):
				lines[y][x] = int(lines[y][x])
		for i in range(0, 100):
			flashed = set()
			for y, line in enumerate(lines):
				for x, number in enumerate(line):
					name = str(x) + "," + str(y)
					if int(number) >= 9:
						lines[y][x] = 0
						flashed.add(name)
						lines, sum, flashed = AffectPerimeter(x, y, lines, sum, flashed)
						sum += 1
					else:
						if name not in flashed:
							lines[y][x] = int(lines[y][x]) + 1


	print(sum)


def D11S2():
	sum = 0
	lines = []
	AllFlash = True
	i=0
	path = "2021_D11.txt"
	with open(path) as file:
		lines = file.readlines()
		lines = [list(line.strip()) for line in lines]
		for y, line in enumerate(lines):
			for x, number in enumerate(line):
				lines[y][x] = int(lines[y][x])
		while(True):
			i += 1
			flashed = set()
			for y, line in enumerate(lines):
				for x, number in enumerate(line):
					name = str(x) + "," + str(y)
					if int(number) >= 9:
						lines[y][x] = 0
						flashed.add(name)
						lines, sum, flashed = AffectPerimeter(x, y, lines, sum, flashed)
						sum += 1
					else:
						if name not in flashed:
							lines[y][x] = int(lines[y][x]) + 1
			AllFlash = True
			for y, line in enumerate(lines):
				for x, number in enumerate(line):
					if number != 0:
						AllFlash = False
						break
				if not AllFlash:
					break
			if AllFlash:
				AllFlash = i
				break
	print(AllFlash)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	D11S2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
