#Comments were added to make it easy to understand
def latest_non_conflict(intervals, i):
    for j in range(i - 1, -1, -1):
        if intervals[j][1] <= intervals[i][0]:
            return j
    return -1

def weighted_interval_scheduling(intervals):
    # Sort intervals based on their end times
    intervals.sort(key=lambda x: x[1])

    # Initialize dp array where dp[i] will store the maximum weight for intervals[0..i]
    n = len(intervals)
    dp = [0] * n

    dp[0] = intervals[0][2]  # Maximum weight including the first interval

    for i in range(1, n):
        # Weight of including the current interval
        incl_weight = intervals[i][2]

        # Find the latest non-conflicting interval with the current interval
        l = latest_non_conflict(intervals, i)
        if l != -1:
            incl_weight += dp[l]

        # Store the maximum of including or not including the current interval
        dp[i] = max(incl_weight, dp[i-1])

    return dp[-1]


# Each interval is represented as a tuple (start_time, end_time, weight)
intervals = [
    (1, 3, 5),
    (2, 5, 6),
    (4, 6, 5),
    (6, 7, 4),
    (5, 8, 11),
    (7, 9, 2)
]

print("Maximum weight of non-overlapping intervals:", weighted_interval_scheduling(intervals))
