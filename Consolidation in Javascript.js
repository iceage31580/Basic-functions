function consolidateIntervals(intervals) {
  intervals.sort(a,b) => a[0] -b[0]); //sort intervals by starting point
  const result = [intervals[0]]; 
  for(let i = 1; i < intervals.length; i++)
    const[prevStart, prevEnd] = result[result.length - 1]; 
    const[currStart, currEnd] = intervals[i]; 
    if(currStart <= prevEnd)
    {
      result[result.length -1][1] = Math.max(prevEnd, currEnd)
    } else {
      result.push([currStart, currEnd]); 
    }
  }
    return result; 
}
