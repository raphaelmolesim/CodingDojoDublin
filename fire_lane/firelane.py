

class FireLane():
	def __init__(self, num_rows, num_cols):
		self.cars = []
		self.fire_lane_position = 0

        #"4 1 3 W"
	def addCar(self, car_info):
		self.cars.append(car_info)


	def result(self):
		matching_cars = []
		for index in range(0, len(self.cars)):
			if self.matches(self.cars[index]):
				matching_cars.append(index)
		return matching_cars

	def matches(self, car):
		car_info = car.split(' ')
		return int(car_info[1]) == self.fire_lane_position
		
#	def occupied_columns(self):
#		columns = []
#		for index in range(0, len(self.cars)):
#			car_info = self.cars[index].split(' ')
#			if (car_info[3] == "E"):
#				columns.append(int(car_info[0]))
#				columns.append(int(car_info[0]) + int(car_info[2]) - 1)
#			if (car_info[3] == "W"):
#				columns.append(car_info[0])
#				columns.append(int(car_info[0]) - int(car_info[2]) + 1)
#			if (car_info[3] == "N" and car_info[3] == "S"):
#				columns.append(int(car_info[0]))
#		return columns	
