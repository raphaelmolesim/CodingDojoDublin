class Rectangle
  def initialize(p1, p2)
    @points = [p1, p2]
  end
  
  def [] (i)
    @points[i]
  end
  
  def overlaps?(other)
    big, small = other, self
    
    # p "#{small[0][0]} <= #{big[1][0]} and #{big[1][0]} <= #{small[1][0]}"
    # p "#{big[0][1]} <= #{small[0][1]} and #{small[0][1]} <= #{big[1][1]}"
    
    small[0][0] < big[1][0] and big[1][0] < small[1][0] and
    small[0][1] < big[1][1] and big[1][1] < small[1][1]
  end
end