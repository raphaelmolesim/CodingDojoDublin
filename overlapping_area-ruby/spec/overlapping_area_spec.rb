require "overlapping_area"

describe "overlapping_area" do
  
  it "should return zero if I don't have retangles" do
    overlapping_area.should == 0
  end
  
  it "should return 1 if I have an overlapping area of 1" do
    overlapping_area([0,0,2,2], [-1,-1,1,1]).should == 1
  end
  
  it "should return 2 if I have an overlapping area of 2" do
    overlapping_area([0,0,2,2], [0,0,2,1]).should == 2
  end
  
  it "should return 1 with x2 and y2 of r1 smaller then x2, y2 of r2" do
    overlapping_area([0,0,2,2], [1,0,2,1]).should == 1
  end
  
  it "should return 2 even if the size of the r2 is 3" do
    overlapping_area([0,0,2,2], [-1,0,2,1]).should == 2
  end
  
end