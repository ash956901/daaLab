def can_form_subset(arr, target):
    def check_subset(arr, target, index):
        if target == 0:
            return True
        
        if index >= len(arr):
            return False
            
        include = check_subset(arr, target - arr[index], index + 1)
        exclude = check_subset(arr, target, index + 1)
        
        # Return True if either include or exclude gives True
        return include or exclude
    
  
    return check_subset(arr, target, 0)


arr = [3, 34, 4, 12, 5, 2]
target = 9

if can_form_subset(arr, target):
    print(f"Yes, there is a way to pick some numbers from {arr} that add up to {target}.")
else:
    print(f"No, it's not possible to pick some numbers from {arr} that add up to {target}.")
