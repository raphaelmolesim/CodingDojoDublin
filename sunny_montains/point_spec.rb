require "point"

describe Point do

	it "should be able to create a instance" do
		Point.new.class.should be == Point
	end
	
	it "should be able to set X and Y" do
		point = Point.new(1, 3)
		point.x.should be == 1
		point.y.should be == 3
	end
	
end
