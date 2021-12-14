path = "D14_Test1.txt"
with open(path) as file:
	lines = file.readlines()
	lines = [line.strip() for line in lines]
	polymer = lines[0]
	lines.__delitem__(0)
	lines.__delitem__(0)
	rules = {}
	letters = {}
	for line in lines:
		key = line.split(" -> ")[0]
		value = line.split(" -> ")[1]
		if value not in letters:
			letters[value] = 0
		rules[key] = value
	for i in range(0, 10):
		newPolymer = ""
		for j in range(0, len(polymer) - 1):
			window = polymer[j] + polymer[j+1]
			newPolymer += polymer[j]
			if window in rules:
				newPolymer += rules[window]
		newPolymer += polymer[len(polymer) - 1]
		polymer = newPolymer

	for c in polymer:
		letters[c] += 1

	valuesList = list(letters.values())
	maxValue = max(valuesList)
	minValue = min(valuesList)

	print(maxValue - minValue)
