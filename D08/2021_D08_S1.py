path = "2021_D08.txt"
sum = 0
numbers = []
lengthSearch = [2,4,3,7]
with open(path) as file:
	lines = file.read().splitlines()
	for i in range(0, len(lines)):
		new = lines[i].split("|")[1].split(" ")
		new = [digit for digit in new if digit != ""]
		numbers.append(new)
		
for row in numbers:
	print(row)
	for digit in row:
		if len(digit) in lengthSearch:
			sum += 1
			
print(sum)