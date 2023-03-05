#include <iostream> 
#include <vector> 
#include <algorithm> 

using namespace std; 

vector<vector<int> consolidate_intervals(vector<vector<int>& intervals)
sort(intervals.begin(), intervals.end()); 

for(const auto& interval : intervals)
{
   if(consolidated.empty() || interval[0] > consolidated.back()[1])
   {
     consolidated.push_back(interval); 
   }
  else
  {
    consolidated.back()[1] = max(consolidated.back[1], interval[1])); 
  }
    return consolidated; 
}

int main() 
{
  vector<vector<int> intervals {{1,2}, {2,5}, {7,10}, {8,11}}; 
  vector<vector<int> consolidated_intervals = consolidated_intervals(intervals); 
  
  for(const auto& interval : consolidated_intervals)
  {
    cout << "[" << interval[0] << ", " << interval[1] << "]" << endl; 
  }
  return 0; 
}
