def overlapping_area (rectangle1=[], rectangle2=[])
  return 0 if rectangle1.empty?
  if rectangle1[2] <= rectangle2[2] or rectangle1[3] <= rectangle2[3]
    return (rectangle2[0]..rectangle2[2]).find_all { |i| i >= rectangle1[0] and i <= rectangle1[2] }.size - 1
  end
  1
end
