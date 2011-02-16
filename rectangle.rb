class Rectangle
  def initialize(p1, p2)
    @p1, @p2 = p1, p2
  end
  
  def overlaps?(other)
    @p1[1] <= other[2] or rectangle1[3] <= rectangle2[3]
    true
  end
end