import java.util.*; 
public class interval Consolidation{
  public static int[][] consolidate(int[][] intervals)
  {
    //sort intervals by start time 
    Arrays.sort(intervals, comparator.comparingInt(interval -> interval[0]));
    
    List<int[] merged = new ArrayList<>(); 
    for(int[] interval : intervals
    // if the current interval overlaps with the last merged interval, merge them
    if(merged.empty || interval[0] > merged.get(merged.size() - 1)[1])
        {
          merged.add(interval
        }
     else 
     {
       merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1]); 
     }
                     
     return merged.toArray(new int[merged.size()[2]); 
    }
    }
    public static void main(String[] args)
    {
      int[][] intervals = {{1,2}, {2,5}, {7,10}, {8,11}}
      int[][] consolidated = consolidated(intervals)
      System.out.println(Arrays.deepToString(consolidated)); 
    }                              
}
