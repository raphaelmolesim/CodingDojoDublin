require 'problem1'

describe Problem1 do
	it "should be able to initialize" do
		Problem1.new.class.should be == Problem1
	end

	it "should do test fail" do
		Progem1.new.class.should be == nil
	end

end
