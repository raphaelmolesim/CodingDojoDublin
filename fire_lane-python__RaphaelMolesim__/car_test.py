import unittest
from car import Car

class CarTest(unittest.TestCase):

	def test_it_should_be_able_to_create_instance(self):
		car = Car("1 1 2 S")
		self.assertEquals(Car, car.__class__)
	
	def test_it_should_be_able_to_assign_car_attributes(self):
		car = Car("1 1 2 S")
		self.assertEquals(1, car.x)
		self.assertEquals(1, car.y)
		self.assertEquals(2, car.lenght)
		self.assertEquals("S", car.direction)	

	def test_it_should_be_able_to_assign_car_attributes_with_biggers_numbers(self):
		car = Car("945 763 25 W")
		self.assertEquals(945, car.x)
		self.assertEquals(763, car.y)
		self.assertEquals(25, car.lenght)
		self.assertEquals("W", car.direction)

	def test_it_should_be_able_to_assign_car_a_id(self):
		car = Car("1 1 2 S")
		car.id = 23
		self.assertEquals(23, car.id)

	def test_it_should_be_able_to_know_where_the_car_start_and_end_with_direction_east(self):
		car = Car("1 1 3 E")
		self.assertEquals((1, 1), car.start)
		self.assertEquals((3, 1), car.end)

	def test_it_should_be_able_to_know_where_the_car_start_with_direction_west(self):
		car = Car("4 6 3 W")
		self.assertEquals((4, 6), car.start)
		self.assertEquals((2, 6), car.end)

	def test_it_should_be_able_to_know_where_the_car_start_with_direction_south(self):
		car = Car("4 2 5 S")
		self.assertEquals((4, 2), car.start)
		self.assertEquals((4, 6), car.end)

	def test_it_should_be_able_to_know_where_the_car_start_with_direction_north(self):
		car = Car("4 7 5 N")
		self.assertEquals((4, 7), car.start)
		self.assertEquals((4, 3), car.end)

	def test_it_should_be_able_to_know_where_is_the_next_place_with_direction_east(self):
		car = Car("1 1 3 E")
		self.assertEquals((4, 1), car.next())

	def test_it_should_be_able_to_know_where_is_the_next_place_with_direction_west(self):
		car = Car("7 1 5 W")
		self.assertEquals((2, 1), car.next())

	def test_it_should_be_able_to_know_where_is_the_next_place_with_direction_south(self):
		car = Car("3 1 3 S")
		self.assertEquals((3, 4), car.next())

	def test_it_should_be_able_to_know_where_is_the_next_place_with_direction_north(self):
		car = Car("5 5 2 N")
		self.assertEquals((5, 3), car.next())
	
	def test_it_should_be_able_to_give_all_the_point_that_a_car_occupies_with_direction_north(self):
		car = Car("2 3 4 N")
		self.assertEquals([(2, 0), (2, 1), (2, 2), (2, 3)], car.occupied_spaces())

	def test_it_should_be_able_to_give_all_the_point_that_a_car_occupies_with_direction_south(self):
		car = Car("2 0 4 S")
		self.assertEquals([(2, 3), (2, 2), (2, 1), (2, 0)], car.occupied_spaces())

	def test_it_should_be_able_to_give_all_the_point_that_a_car_occupies_with_direction_east(self):
		car = Car("2 3 4 E")
		self.assertEquals([(5, 3), (4, 3), (3, 3), (2, 3)], car.occupied_spaces())

	def test_it_should_be_able_to_give_all_the_point_that_a_car_occupies_with_direction_west(self):
		car = Car("5 3 4 W")
		self.assertEquals([(2, 3), (3, 3), (4, 3), (5, 3)], car.occupied_spaces())

if __name__ == '__main__':
	unittest.main()
