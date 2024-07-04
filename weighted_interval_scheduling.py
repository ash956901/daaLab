def weighted_interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort intervals by finish time
    
    memo = {}
    
    def recurse(index):
        if index < 0:
            return 0
        
        if index in memo:
            return memo[index]
        
        # Find the latest non-overlapping interval before the current one
        latest_non_overlap = -1
        for i in range(index - 1, -1, -1):
            if intervals[i][1] <= intervals[index][0]:
                latest_non_overlap = i
                break
        
        # Calculate maximum weight by either including or excluding the current interval
        include = intervals[index][2] + (recurse(latest_non_overlap) if latest_non_overlap != -1 else 0)
        exclude = recurse(index - 1)
        
        # Memoize the result
        memo[index] = max(include, exclude)
        
        return memo[index]
    
    return recurse(len(intervals) - 1)

# Example usage:
intervals = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (7, 8, 7)]
print(weighted_interval_scheduling(intervals))  
