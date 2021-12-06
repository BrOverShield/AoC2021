import csv



Path = "2021_D06.txt"
last = 0
fishes = {"0" : 0,"1" : 0,"2" : 0,"3" : 0,"4" : 0,"5" : 0,"6" : 0,"7" : 0,"8" : 0}
with open(Path) as File:
	timers = File.read().strip().split(",")
	for timer in timers:
		fishes[timer] += 1
		
	for i in range (0, 256):
		newFishes = fishes["0"]
		fishes["0"] = fishes["1"]
		fishes["1"] = fishes["2"]
		fishes["2"] = fishes["3"]
		fishes["3"] = fishes["4"]
		fishes["4"] = fishes["5"]
		fishes["5"] = fishes["6"]
		fishes["6"] = fishes["7"] + newFishes
		fishes["7"] = fishes["8"]
		fishes["8"] = newFishes
		
	print(sum(list(fishes.values())))