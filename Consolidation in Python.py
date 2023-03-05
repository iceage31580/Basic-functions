def consolidate _intervals(intervals):
  # Sort the intervals based on their start times
  intervals.sort(key=lambda x: x[0])
  
  # Initialize the result list and the current interval
  result = []
  current = []
  
  # Loop through the intervals 
  for interval in intervals:
  # If the current interval is empty or does not overlap with the current interval, add the current interval
  #Add the current interval to the result list and update the current interval to the current interval
  if not current or interval[0] > current[1]:
    current = interval
    result.append(current)
  # If the current interval overlaps with the current interval, update the end time fo the current interval
  # update the end time of the current interval to the maximum of its current end time
  else: 
      current[1] = max(current[1], interval[i])
  return result

