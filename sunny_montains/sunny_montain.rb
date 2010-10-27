class SunnyMontain

	attr_accessor :points

	def hyp(p1, p2)
		square1 =  p1.x - p2.x 
		square1 = square1 * square1
		
		square2 = p1.y - p2.y
		square2 = square2 * square2
	
		Math.sqrt(square1 + square2)	
	end
	
	def length_of_sunshine
		i = 0
		total_len = 0.0
		max_y = -1
		
		(points.size-1).times do
			puts(total_len)
			if (max_y < points[i+1].y)
				
				max_y = points[i+1].y
		  	total_len += hyp(points[i], points[i+1]) 
		  end
		  i = i + 1
		end
		
		total_len		
	end

	def initialize()
		@points = []
	end
	
	def magic_hypothenuse(p1, p2, y)
		hyp1 = hyp(p1, p2)
		height1 = p1.y.to_f - p2.y.to_f
		height2 = p1.y.to_f - y
		(hyp1 * height2)/height1
	end
end
