path = "2021_D01.txt"
lines = [line for line in open(path)]
depth = int(lines[0])
sum = 0
first = True
for line in lines:
	if first:
		first = False
		continue
	else:
		if int(line) > depth:
			sum += 1
		depth = int(line)
		
print("Answer: " + str(sum))