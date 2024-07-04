def weighted_interval_scheduling(intervals):
    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])
    
    # Precompute the p values
    p = [0] * len(intervals)
    for j in range(len(intervals)):
        i = j - 1
        while i >= 0 and intervals[i][1] > intervals[j][0]:
            i -= 1
        p[j] = i + 1

    # Compute the maximum weight using dynamic programming
    dp = [0] * (len(intervals) + 1)
    for j in range(1, len(intervals) + 1):
        dp[j] = max(dp[j-1], intervals[j-1][2] + dp[p[j-1]])

    return dp[-1]

# Example usage:
intervals = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 4), (5, 8, 11), (7, 9, 2)]
max_weight = weighted_interval_scheduling(intervals)
print(max_weight)
