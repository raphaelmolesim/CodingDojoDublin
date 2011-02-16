class Rectangle
  def initialize(p1, p2)
    @points = [p1, p2]
  end
  
  def [] (i)
    @points[i]
  end
  
  def overlaps?(other)
    (self[1][0] >= other[1][0] or self[1][1] >= other[1][1]) and
    
  end
end