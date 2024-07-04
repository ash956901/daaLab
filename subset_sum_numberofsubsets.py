def subset_sum(nums, target):
    memo = {}

    def recurse(index, current_sum):
        if current_sum == target:
            return 1  # Found a subset that sums up to the target
        
        if index >= len(nums):
            return 0  # Reached the end of the array
        
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]
        
        # Count subsets including and excluding current number
        include = recurse(index + 1, current_sum + nums[index])
        exclude = recurse(index + 1, current_sum)
        
        # Total count is sum of both cases
        total_count = include + exclude
        
        memo[(index, current_sum)] = total_count
        return total_count
    
    return recurse(0, 0)

nums = [2, 4, 6, 8]
target = 10
print(subset_sum(nums, target))  
