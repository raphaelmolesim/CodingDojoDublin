require "rectangle"

describe Rectangle do
  it "should create a new rectangle with 2 arrays" do
    Rectangle.new([0,0], [1,1]).should be_an Rectangle
  end
  
  it "should know if a rectangle overlaps another" do
    r1 = Rectangle.new([0,0], [2,2])
    r2 = Rectangle.new([0,0], [1,1])
    
    r1.overlaps?(r2).should be_true
  end

  it "should know if a rectangle does not overlap another" do
    r1 = Rectangle.new([0,0] , [2,2])
    r2 = Rectangle.new([-3,-3], [-1,-1])
    
    r1.overlaps?(r2).should be_false
  end

  it "should know if a rectangle does not overlap another" do
    r1 = Rectangle.new([0,0] , [2,2])
    r2 = Rectangle.new([-2,-2], [-0,-0])
    
    r1.overlaps?(r2).should be_false
  end
end