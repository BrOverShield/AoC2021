import csv

path = "2021_D03.txt"
MostCommon = []
gamma = ""
epsilon = ""
lines = []
with open(path) as file:
	reader = csv.reader(file)
	lines = list(reader)
	MostCommon = [0] * (len(lines[0][0]))
	for row in lines:
		for i, c in enumerate(row[0]):
			if c == "1":
				MostCommon[i] += 1
	
for line in MostCommon:
	if line > (len(lines)/2):
		gamma += "1"
		epsilon += "0"
	else:
		gamma += "0"
		epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)