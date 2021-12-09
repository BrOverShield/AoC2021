path = "2021_D08.txt"
sum = 0
numbersList = []
resultsList = []
lengthSearch = [2,4,3,7]
with open(path) as file:
	lines = file.read().splitlines()
	for i in range(0, len(lines)):
		lineNumbers = lines[i].split("|")[0].strip().split(" ")
		lineResults = lines[i].split("|")[1].strip().split(" ")
		numbersList.append(lineNumbers)
		resultsList.append(lineResults)

for i, numbers in enumerate(numbersList):
	one = [number for number in numbers if len(number) == 2][0]
	seven = [number for number in numbers if len(number) == 3][0]
	segmentA = "x"
	for c in seven:
		if c not in list(one):
			segmentA = c
			break
	four = [number for number in numbers if len(number) == 4][0]
	possibilities = [number for number in numbers if len(number) == 6]
	segmentC = "x"
	for possibility in possibilities:
		for c in list(one):
			if c not in list(possibility):
				segmentC = c
				break
		if segmentC != "x":
			break
	
	
	
	
	
	fullNumber = ""
	for number in resultsList[i]:
		if len(number) == 2:
			fullNumber += "1"
		elif len(number) == 3:
			fullNumber += "7"
		elif len(number) == 4:
			fullNumber += "4"
		elif len(number) == 7:
			fullNumber += "8"
		elif len(number) == 6:
			if set(four) <= set(number):
				fullNumber += "9"
			elif segmentC in set(number):
				fullNumber += "0"
			else:
				fullNumber += "6"
		elif len(number) == 5:
			if set(one) <= set(number):
				fullNumber += "3"
			elif segmentC in set(number):
				fullNumber += "2"
			else:
				fullNumber += "5"
		else:
			print("error")
	sum += int(fullNumber)
print(sum)