require "sunny_montain"
require "point"

describe SunnyMontain do

	it "should be able to create a instance" do
		SunnyMontain.new.class.should be == SunnyMontain
	end
	
	it "should be able to receive the graph" do
		@sunny = SunnyMontain.new
		@sunny.points << Point.new(0, 1)
		@sunny.points.size.should be == 1
	end
	
	it "should return sunny distance between 2 points (simplest case)" do
	  point1 = Point.new(0, 10)
	  point2 = Point.new(1, 9)

	 
	  
	  @sunny_montain.distance_covered(point1, point2).should be == Math.sqrt(2)
	  
	
	end

end
