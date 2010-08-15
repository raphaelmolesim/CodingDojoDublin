import unittest
from firelane import FireLane
from car import 

class FireLaneTest(unittest.TestCase):

	def test_acceptance_1(self):
		obj = FireLane(8,8)
		obj.number_cars = 5
		obj.fire_lane_position = 3
		obj.addCar("1 0 4 E")
		obj.addCar("4 1 3 W")
		obj.addCar("2 4 3 S")
		obj.addCar("3 3 3 E")
		obj.addCar("1 2 2 N")
		#self.assertEquals( [0, 3, 4, 1], obj.result())


	def test_one_car_in_the_lane(self):
                obj = FireLane(8,8)
                obj.number_cars = 1
                obj.fire_lane_position = 3
                obj.addCar("4 1 3 W")
                self.assertEquals( [0], obj.result())

	def test_one_car_outside_the_lane(self):
                obj = FireLane(8,8)
                obj.number_cars = 1
                obj.fire_lane_position = 3
                obj.addCar("0 0 1 W")
                self.assertEquals( [] obj.result())


	def test_result_array_of_cars(self):
		obj = FireLane(4,4)
		obj.addCar("1 0 2 E")
		self.assertEquals([1,2], obj.occupied_columns()) 


if __name__ == '__main__':
	unittest.main()
