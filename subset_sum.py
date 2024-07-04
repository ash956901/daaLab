def subset_sum(nums, target):
    memo = {}

    def recurse(index, current_sum):
        if current_sum == target:
            return True
        if index >= len(nums):
            return False
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]
        
        include = recurse(index + 1, current_sum + nums[index])
        exclude = recurse(index + 1, current_sum)
        result = include or exclude
        
        memo[(index, current_sum)] = result
        return result
    
    return recurse(0, 0)

nums = [2, 4, 6, 8]
target = 10
print(subset_sum(nums, target))  
