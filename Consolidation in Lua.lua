function consoludate(intervals)
  --sort the intervals based on their start time
  table.sort(intervals, function(a,b) return a[1] < b[1] end)
  
  local consolidated = {}
  local current = intervals[1]
  
  --iterate through each interval and consolidates if neccessary 
  for i = 2 # intervals do
  local interval = intervals[i]
    if interval[1] <= current[2] then
      current[2] = math.max(current[2], interval[2])
    else
      table.insert(consolidated, current)
      current = interval
    end
 end
table.insert(consolidated, current)
return consolidated

  end
