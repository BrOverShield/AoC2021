path = "2021_D07.txt"

fuel = {}
with open(path) as file:
	positions = file.read().split(",")
	maximum = max(positions)
	minimum = min(positions)
	for i in range(int(minimum), int(maximum)):
		fuel[i] = 0
		for position in positions:
			higher = max(int(position) , i)
			lower = min(int(position) , i)
			fuel[i] += (higher - lower)
			
valuesList = list(fuel.values())
lowest = min(valuesList)

print(lowest)