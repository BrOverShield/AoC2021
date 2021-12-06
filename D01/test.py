data = [line.strip() for line in open("2021_D01.txt", 'r')]

counter = 0
pos = [0, 0]
last = 0

for i, line in enumerate(data):
    if int(line) > last:
        counter += 1

    last = int(line)
	
print(counter)