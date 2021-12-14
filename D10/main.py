# This is a sample Python script.

import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
openingBrackets = ["(", "[", "{", "<"]
closingBrackets = [")", "]", "}", ">"]
FILO = []

def calculatePoints(input):
	if input == ")":
		return 3
	elif input == "]":
		return 57
	elif input == "}":
		return 1197
	elif input == ">":
		return 25137
	else:
		return 0

def calculatePointsPart2(input):
	if input == ")":
		return 1
	elif input == "]":
		return 2
	elif input == "}":
		return 3
	elif input == ">":
		return 4
	else:
		return 0

def calculateExpected(input):
	expected = "x"
	if input == "(":
		expected = ")"
	elif input == "[":
		expected = "]"
	elif input == "{":
		expected = "}"
	elif input == "<":
		expected = ">"
	return expected


def D10S1():
	sum = 0
	path = "2021_D10_S1_Test1.txt"
	with open(path) as file:
		lines = file.readlines()
		lines = [line.strip() for line in lines]
		for line in lines:
			print(line)
			FILO = []
			imposter = "x"
			for c in line:
				if c in openingBrackets:
					closingBracket = calculateExpected(c)
					FILO.append(closingBracket)
				else:
					if FILO[len(FILO)-1] == c:
						FILO.__delitem__(len(FILO)-1)
					else:
						imposter = c
						break
			sum += calculatePoints(imposter)
	print(sum)

def D10S2():
	sum = 0
	scores = []
	path = "2021_D10.txt"
	with open(path) as file:
		lines = file.readlines()
		lines = [line.strip() for line in lines]
		for line in lines:
			FILO = []
			imposter = "x"
			for c in line:
				if c in openingBrackets:
					closingBracket = calculateExpected(c)
					FILO.append(closingBracket)
				else:
					if FILO[len(FILO) - 1] == c:
						FILO.__delitem__(len(FILO) - 1)
					else:
						imposter = c
						break
			if imposter == "x":
				FILO.reverse()
				#print(FILO)
				score = 0
				for c in FILO:
					score *= 5
					score += calculatePointsPart2(c)
				scores.append(score)
	scores = sorted(scores)
	print(scores[math.floor(len(scores)/2)])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	D10S2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
