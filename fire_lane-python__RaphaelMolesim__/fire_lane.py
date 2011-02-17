from printer import Printer

class FireLane():

	def __init__(self, rows, cols, lane):
		self.cars = []
		self.points = {}
		self.lane = lane
		self.printer = Printer(rows, cols, lane)

	def addCar(self, car):
		car.id = len(self.cars)
		self.cars.append(car)

	def numberOfCars(self):
		return len(self.cars)

	def carsThatIHaveToMove(self):
		self.generate_points(self.cars)
		cars_which_should_move = []
		for car in self.cars:
			if (self.isOnTheLane(car)):
				cars_which_should_move.append(self.which_cars_should_I_move_to_move_this_car(car)) 
		return flatten(cars_which_should_move)

	def which_cars_should_I_move_to_move_this_car(self, car):
		if (self.canIMoveThisCar(car)):
			return [car.id]		
		blocking_car = self.get_blocking_car(car)
		return [car.id , self.which_cars_should_I_move_to_move_this_car(blocking_car)]

	def get_blocking_car(self, car):
		return self.cars[self.points[car.next()]]

	def canIMoveThisCar(self, car):
		return not self.points.has_key(car.next())

	def isOnTheLane(self, car):
		return not self.before(car.start[0], car.end[0]) and not self.after(car.start[0], car.end[0])

	def before(self, start, end):
		return (start < self.lane and end < self.lane)

	def after(self, start, end):
		return (self.lane + 1 < start and self.lane + 1 < end)

	def draw(self):
		self.printer.print_board(self.cars, self.points)

	def generate_points(self, cars):
		for i in range(0, len(cars)):
			for space in cars[i].occupied_spaces():
				self.points[space] = i
			
def flatten(array):
	out = []
	for item in array:
		if isinstance(item, (list, tuple)):
			out.extend(flatten(item))
		else:
			out.append(item)
	return out
