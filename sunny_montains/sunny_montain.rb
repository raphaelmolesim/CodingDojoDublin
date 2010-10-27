class SunnyMontain

	attr_accessor :points

	def distance_covered (p1, p2)
		square1 =  p1.x - p2.x 
		square1 = square1**
		
		square2 = p1.y - p2.y
		square2 = square2**
		
		puts square1
		puts square2		
	
		Math.sqrt(square1 + square2)	
	end

	def initialize()
		@points = []
	end
end
