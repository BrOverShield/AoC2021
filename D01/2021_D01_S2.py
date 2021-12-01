import timeit

def star2()
	path = "2021_D01.txt"
	lines = [line for line in open(path)]
	measurement = int(lines[0]) + int(lines[1]) + int(lines[2])
	sum = 0
	for i in range(1,len(lines) - 2) :
		measurement2 = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
		if measurement < measurement2:
			sum += 1
		measurement = measurement2
			
	print("Answer: " + str(sum))
	
timeit()