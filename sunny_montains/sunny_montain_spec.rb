require "sunny_montain"
require "point"

describe SunnyMontain do

	before do
		@sunny = SunnyMontain.new
	end

	it "should be able to create a instance" do
		SunnyMontain.new.class.should be == SunnyMontain
	end
	
	it "should be able to receive the graph" do
		@sunny.points << Point.new(1, 0)
		@sunny.points.size.should be == 1
	end
	
	it "should return sunny distance between 2 points (simplest case)" do
	  point1 = Point.new(10, 0)
	  point2 = Point.new(9, 1)

	  @sunny.hyp(point1, point2).should be == Math.sqrt(2)	
	end
	
	it "should return distance between 2 different points" do
		point1 = Point.new(10, 0)
		point2 = Point.new(8, 1)
		
		@sunny.hyp(point1, point2).should be == Math.sqrt(5)
	end
	
	it "should calculating length of shadow" do
		@sunny.points << Point.new(10, 0)
		@sunny.points << Point.new(8, 1)
		@sunny.points << Point.new(6, 2)
		
		@sunny.length_of_shadow.should be == Math.sqrt(5) + Math.sqrt(5)
	end
	
	

end
