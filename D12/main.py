# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
alreadyExplored = set()
smallCavesExplored = set()
Path = []
Paths = []
nodes = {}
twice = False

class Node:
	def __init__(self, name):
		self.name = name
		self.connections = []

def ExploreNode(node):
	#global alreadyExplored
	#global Path
	#global Paths
	for pathNode in node.connections:
		if pathNode == "end" and Path not in Paths:
			Paths.append(Path.copy())
		elif pathNode not in alreadyExplored:
			if pathNode == pathNode.lower():
				alreadyExplored.append(pathNode)
			Path.append(pathNode)
			ExploreNode(nodes[pathNode])
			Path.pop()
			if pathNode == pathNode.lower() and pathNode != "end":
				alreadyExplored.pop()

def ExploreNodePart2(node):
	global twice
	#global alreadyExplored
	#global Path
	#global Paths
	for pathNode in node.connections:
		if pathNode == "end" and Path not in Paths:
			Paths.append(Path.copy())
		elif pathNode not in alreadyExplored:
			if pathNode == pathNode.lower():
				if not twice:
					if pathNode in smallCavesExplored:
						alreadyExplored.add(pathNode)
						twice = True
					else:
						smallCavesExplored.add(pathNode)
				else:
					if pathNode in smallCavesExplored:
						continue
					else:
						smallCavesExplored.add(pathNode)
			Path.append(pathNode)
			ExploreNodePart2(nodes[pathNode])
			Path.pop()
			if pathNode == pathNode.lower():
				if pathNode in smallCavesExplored and pathNode in alreadyExplored:
					twice = False
					alreadyExplored.remove(pathNode)
				else:
					smallCavesExplored.remove(pathNode)

def D12S1():
	global nodes
	global alreadyExplored
	global Path
	global Paths
	filePath="2021_D12.txt"
	with open(filePath) as file:
		lines = file.readlines()
		lines = [line.strip() for line in lines]
		for line in lines:
			node1 = line.split("-")[0]
			node2 = line.split("-")[1]
			if node1 not in nodes:
				nodes[node1] = Node(node1)
			if node2 not in nodes:
				nodes[node2] = Node(node2)
			nodes[node1].connections.append(node2)
			nodes[node2].connections.append(node1)

	alreadyExplored.append("start")
	ExploreNode(nodes["start"])
	print(len(Paths))

def D12S2():
	global nodes
	global alreadyExplored
	global Path
	global Paths
	filePath="2021_D12.txt"
	with open(filePath) as file:
		lines = file.readlines()
		lines = [line.strip() for line in lines]
		for line in lines:
			node1 = line.split("-")[0]
			node2 = line.split("-")[1]
			if node1 not in nodes:
				nodes[node1] = Node(node1)
			if node2 not in nodes:
				nodes[node2] = Node(node2)
			nodes[node1].connections.append(node2)
			nodes[node2].connections.append(node1)

	alreadyExplored.add("start")
	smallCavesExplored.add("start")
	ExploreNodePart2(nodes["start"])
	for a in Paths:
		print(a)
	print(len(Paths))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
D12S2()