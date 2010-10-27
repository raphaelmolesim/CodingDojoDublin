require "sunny_montains"
require "point"
describe SunnyMontains do

	it "should be able to create a instance" do
		SunnyMontains.new.class.should be == SunnyMontains
	end
	
	it "should be able to receive the graph" do
		@sunny = SunnyMontains.new
		@sunny.points << Point.new(0, 1)
		@sunny.points.size.should be == 1
	end

end
