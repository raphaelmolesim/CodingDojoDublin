require "point"

describe Point do

	it "should be able to create a instance" do
		Point.new.class.should be == Point
	end
	
end
