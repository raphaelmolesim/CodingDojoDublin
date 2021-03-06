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
		
		
		max_y = 0 
		
		(points.size-1).times do
			if max_y == 0
				total_len += hyp(points[i], points[i+1])
				max_y = points[i+1].y
			else
				if (max_y < points[i+1].y)
					height = magic_hypothenuse(points[i], points[i+1], max_y)
					total_len += height
					max_y = points[i+1].y	
					
				end		
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
		return hyp1 if (p1.y == y)
		height1 = p1.y.to_f - p2.y.to_f
		height2 = p1.y.to_f - y
		(hyp1 * height2)/height1
	end
end
