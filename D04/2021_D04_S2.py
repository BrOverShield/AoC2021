import csv

def makeDictionaryList(line):
	result = {}
	for i in line:
		result[i] = False
	return result
	
def CheckLine(Line):
	win = True
	for value in line.values():
		if value == False:
			win = False
			break
	return win
	
def CheckColumn(board, index):
	win = True
	for line in board:
		if list(line.values())[index] == False:
			win = False
			break
	return win
	
def CalculateSum(board):
	sum = 0
	for line in board:
		numbers = list(line.keys())
		marked = list(line.values())
		for i, mark in enumerate(marked):
			if not mark:
				sum += int(numbers[i])
	return sum

orderPath = "D04_Order.txt"
boardsPath = "D04_Boards.csv"
boards = []
WinningNumber = 0
with open(orderPath) as orderFile:
	order = orderFile.read().split(",")
	with open(boardsPath) as BoardsFile:
		lines = csv.reader(BoardsFile)
		lines = list(lines)
		
		for i in range(0, len(lines), 5):
			board = []
			board.append(makeDictionaryList(lines[i]))
			board.append(makeDictionaryList(lines[i+1]))
			board.append(makeDictionaryList(lines[i+2]))
			board.append(makeDictionaryList(lines[i+3]))
			board.append(makeDictionaryList(lines[i+4]))
			boards.append(board)
exclude = []
for i, number in enumerate(order):
	for j, board in enumerate(boards):
		if j not in exclude:
			for line in board:
				if number in line:
					line[number] = True
					if i >= 5:
						if CheckLine(line):
							exclude.append(j)
							break
						index = list(line.keys()).index(number)
						if CheckColumn(board, index):
							exclude.append(j)
							break
		if len(exclude) == len(boards):
			break
	if len(exclude) == len(boards):
		index = exclude[len(exclude)-1]
		sum = CalculateSum(boards[index])
		WinningNumber = number
		break

print(int(WinningNumber) * int(sum))
