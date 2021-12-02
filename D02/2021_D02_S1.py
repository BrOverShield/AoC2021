import csv

path = "2021_D02.csv"
x = 0
y = 0
with open(path) as file:
	reader = csv.reader(file)
	for row in reader:
		if row[0] == "forward":
			#print("FORWARD")
			x += int(row[1])
		elif row[0] == "down":
			#print("DOWN")
			y += int(row[1])
		elif row[0] == "up":
			#print("UP")
			y -= int(row[1])
		else:
			print("WRONG COMMAND")
			
print(x * y)