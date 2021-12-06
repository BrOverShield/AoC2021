import csv

Path = "2021_D06.txt"
last = 0
with open(Path) as File:
	timers = File.read().strip().split(",")
	for i in range(0, 80):
		newTimers = []
		for i, timer in enumerate(timers):
			i = int(i)
			if timers[i] == 0:
				newTimers.append(8)
				timers[i] = 6
			else:
				timers[i] = int(timers[i]) - 1
		timers += newTimers
		now = len(timers)
	print(len(timers))
		
