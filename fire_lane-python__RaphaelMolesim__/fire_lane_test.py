import unittest
from fire_lane import FireLane
from car import Car

class FireLaneTest(unittest.TestCase):

	def setUp(self):
        	self.board = FireLane(4, 4, 1)
		self.board_big = FireLane(8, 8, 3)

	def test_it_should_be_able_to_create_instance(self):
		self.assertEquals(FireLane, self.board.__class__)

	def test_it_should_be_able_to_add_cars(self):
		self.board.addCar(Car("0 0 1 W"))
		self.assertEquals(1, self.board.numberOfCars())
	
	def test_it_should_be_able_to_two_add_cars(self):
		self.board.addCar(Car("0 0 1 W"))
		self.board.addCar(Car("1 3 2 S"))
		self.assertEquals(2, self.board.numberOfCars())

	def test_it_should_be_able_to_say_which_cars_I_have_to_move_when_I_have_only_one_car_on_the_lane(self):
		self.board.addCar(Car("1 1 1 E"))
		self.assertEquals([0], self.board.carsThatIHaveToMove())

	def test_it_should_be_able_to_say_which_cars_I_have_to_move_when_I_have_one_car_but_not_on_the_lane(self):
		self.board.addCar(Car("0 1 1 E"))
		self.assertEquals([], self.board.carsThatIHaveToMove())

	def test_it_should_be_able_to_say_which_cars_I_have_to_move_when_I_have_only_one_car_on_the_lane_with_bigger_board(self):
		self.board_big.addCar(Car("2 1 2 E"))
		self.assertEquals([0], self.board_big.carsThatIHaveToMove())

	def test_it_should_be_able_to_say_which_cars_I_have_to_move_when_I_have_two_cars_on_the_lane_with_bigger_board(self):
		self.board_big.addCar(Car("2 1 2 E"))
		self.board_big.addCar(Car("2 3 3 E"))
		self.assertEquals([0, 1], self.board_big.carsThatIHaveToMove())

	def test_it_should_be_able_to_say_which_cars_I_have_to_move_when_I_have_two_cars_on_the_lane_with_bigger_board_and_one_in_west_direction(self):
		self.board_big.addCar(Car("2 1 2 E"))
		self.board_big.addCar(Car("6 3 3 W"))
		self.assertEquals([0, 1], self.board_big.carsThatIHaveToMove())

	def test_it_should_be_able_to_say_which_cars_I_have_to_move_when_I_have_one_car_on_the_lane_and_other_out_of_the_lane_with_bigger_board_and_one_in_south_direction(self):
		self.board_big.addCar(Car("2 1 2 E"))
		self.board_big.addCar(Car("6 3 3 S"))
		self.assertEquals([0], self.board_big.carsThatIHaveToMove())

	def test_it_should_be_able_to_say_which_cars_I_have_to_move_when_I_have_one_car_on_the_lane_and_other_out_of_the_lane_with_bigger_board_and_one_in_north_direction(self):
		self.board_big.addCar(Car("2 1 2 E"))
		self.board_big.addCar(Car("6 3 3 N"))
		self.assertEquals([0], self.board_big.carsThatIHaveToMove())
	
	def test_it_should_be_able_to_say_which_cars_I_have_to_move_when_I_have_one_car_on_the_lane_and_other_blocking_his_the_movement(self):
		self.board_big.addCar(Car("3 3 3 W"))
		self.board_big.addCar(Car("6 3 3 S"))
		self.board_big.addCar(Car("0 3 3 N"))
		result = self.board_big.carsThatIHaveToMove()		
		self.assertEquals([0, 2], result)
		
	def test_it_should_be_able_to_say_which_cars_I_have_to_move_when_I_have_one_car_blocking_other_that_are_on_lane(self):
		self.board_big.addCar(Car("0 3 3 N"))
		self.board_big.addCar(Car("3 3 3 W"))
		self.board_big.addCar(Car("6 3 3 S"))
		result = self.board_big.carsThatIHaveToMove()	
		self.assertEquals([1, 0], result)

	def test_it_should_be_able_to_say_which_cars_I_have_to_move_when_I_have_one_car_blocking_other_that_arent_on_lane(self):
		self.board_big.addCar(Car("0 3 3 N"))
		self.board_big.addCar(Car("2 3 2 W"))
		self.board_big.addCar(Car("6 3 3 S"))
		result = self.board_big.carsThatIHaveToMove()
		self.assertEquals([], result)


if __name__ == '__main__':
	unittest.main()
