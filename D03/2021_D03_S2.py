import csv

def getMostCommon(index, lines):
	ones = []
	zeros = []
	for line in lines:
		if line[index] == "1":
			ones.append(line)
		else:
			zeros.append(line)
	if len(zeros) > len(lines)/2:
		return zeros
	else:
		return ones
		
def getLeastCommon(index, lines):
	ones = []
	zeros = []
	for line in lines:
		if line[index] == "1":
			ones.append(line)
		else:
			zeros.append(line)
	if len(ones) < len(lines)/2:
		return ones
	else:
		return zeros

path = "2021_D03.txt"
lines = []
oxygen = 0
co2 = 0
with open(path) as file:
	reader = csv.reader(file)
	lines = list(reader)
	originalLines = [line[0] for line in lines]
	lines = originalLines
	for i in range(0,len(lines[0])):
		if len(lines) == 1:
			break
		lines = getMostCommon(i, lines)
	oxygen = lines[0]
	
	lines = originalLines
	for i in range(0,len(lines[0])):
		if len(lines) == 1:
			break
		lines = getLeastCommon(i, lines)
	co2 = lines[0]

oxygen = int(oxygen, 2)
co2 = int(co2, 2)

print(oxygen * co2)