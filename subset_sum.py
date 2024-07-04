def max_subset_sum(arr, target):
    def max_subset(arr, index, current_sum, target):
        if index == len(arr):
            return current_sum if current_sum <= target else float('-inf')
        
        include = max_subset(arr, index + 1, current_sum + arr[index], target)
        exclude = max_subset(arr, index + 1, current_sum, target)
        
        return max(include, exclude)
    
    return max_subset(arr, 0, 0, target)
  
arr = [3, 7, 2, 8, 4]
target = 10

print("Maximum sum of subset <= target:", max_subset_sum(arr, target))
