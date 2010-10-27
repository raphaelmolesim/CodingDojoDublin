require "sunny_montain"

describe SunnyMontain do

	it "should be able to create a instance" do
		SunnyMontain.new.class.should be == SunnyMontain
	end
	
	it "should be able to receive the graph" do
		@sunny = SunnyMontain.new
		@sunny.points << Point.new(0, 1)
		@sunny.points.size.should be == 1
	end

end
