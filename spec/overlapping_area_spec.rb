require "overlapping_area"

describe OverlappingArea do
  
  it "should be to able to createa instance" do
    OverlappingArea.new.should be_an OverlappingArea
  end
  
  it "should return zero if I don't have retangles" do
    overlapping_area.should == 0
  end
  
  it "should return 1 if I have an overlapping area of 1" do
    overlapping_area([0,0,2,2], [-1,-1,1,1]).should == 1
  end
  
  it "should return 2 if I have an overlapping area of 2" do
    overlapping_area([0,0,2,2], [0,0,2,1]).should == 2
  end
  
end