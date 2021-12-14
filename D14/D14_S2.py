path = "D14.txt"
with open(path) as file:
	lines = file.readlines()
	lines = [line.strip() for line in lines]
	polymer = lines[0]
	lines.__delitem__(0)
	lines.__delitem__(0)
	rules = {}
	letters = {}
	pairs = {}
	for line in lines:
		key = line.split(" -> ")[0]
		value = line.split(" -> ")[1]
		if value not in letters:
			letters[value] = 0
		rules[key] = value
	for c in polymer:
		letters[c] += 1
	pairs = rules.copy()
	for key in list(pairs.keys()):
		pairs[key] = 0
	for i in range(0, len(polymer)-1):
		name = polymer[i] + polymer[i+1]
		pairs[name] += 1
	keys = list(rules.keys())
	values = list(rules.values())
	newPairs = pairs.copy()
	for j in range(0,40):
		for i in range(0, len(rules)):
			pair = keys[i]
			ajout = rules[pair]
			amount = pairs[pair]
			A = pair[0]
			B = pair[1]
			letters[ajout] += amount
			name = A + ajout
			newPairs[name] += amount
			name = ajout + B
			newPairs[name] += amount
			newPairs[pair] -= amount
		pairs = newPairs.copy()
	print(letters)

	maxValue = max(list(letters.values()))
	minValue = min(list(letters.values()))

	print(maxValue - minValue)
