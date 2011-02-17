class Car():

	def __init__(self, data):
		info = data.split(" ")			
		self.x = int(info[0])
		self.y = int(info[1])
		self.lenght = int(info[2])
		self.direction = info[3]
		self.spaces = []
		self.defineStartAndEnd()

	def defineStartAndEnd(self):
		self.start = (self.x, self.y)
		if (self.direction == "E"):
			self.end = (self.x + self.lenght - 1, self.y)
		elif (self.direction == "W"):
			self.end = (self.x - self.lenght + 1, self.y)
		elif (self.direction == "S"):
			self.end = (self.x, self.y + self.lenght - 1)
		elif (self.direction == "N"):
			self.end = (self.x, self.y - self.lenght + 1)
		
	def next(self):
		if (self.direction == "E"):
			return (self.end[0] + 1, self.end[1])
		elif (self.direction == "W"):
			return (self.end[0] - 1, self.end[1])
		elif (self.direction == "S"):
			return (self.end[0], self.end[1] + 1)
		elif (self.direction == "N"):
			return (self.end[0], self.end[1] - 1)

	def occupied_spaces(self):
		if (self.spaces == []):
			if (self.direction == "E"):
				for i in range(self.x, self.x + self.lenght):
					self.spaces.append((i, self.y))
				self.spaces.reverse()
			if (self.direction == "W"):
				for i in range(self.x - self.lenght, self.x):					
					self.spaces.append((i + 1, self.y))
			if (self.direction == "S"):
				for i in range(self.y, self.y + self.lenght):
					self.spaces.append((self.x, i))
				self.spaces.reverse()
			if (self.direction == "N"):
				for i in range(self.y - self.lenght, self.y):
					self.spaces.append((self.x, i + 1))
		return self.spaces
