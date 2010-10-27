class SunnyMontain

	attr_accessor :points

	def hyp(p1, p2)
		square1 =  p1.x - p2.x 
		square1 = square1 * square1
		
		square2 = p1.y - p2.y
		square2 = square2 * square2
	
		Math.sqrt(square1 + square2)	
	end
	
	def length_of_shadow
		i=0
		total_len = 0.0
		
		(points.size-1).times do
		  total_len += hyp(points[i], points[i+1])
		  i=i+1
		end
		
		total_len
		
	end

	def initialize()
		@points = []
	end
end
