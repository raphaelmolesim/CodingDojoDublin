class OverlappingArea
  
  
  
end

def overlapping_area (rectangle1=[], rectangle2=[])
  return 0 if rectangle1 and rectangle2
  return 2 if rectangle1[2] <= rectangle2[2] or rectangle1[3] <= rectangle2[3]
  1
end