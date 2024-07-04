def knapsack(items, i, curr_weight, weight, dp):
    if i >= len(items):
        return 0
       
    if dp[i][curr_weight] != -1:
        return dp[i][curr_weight]
    
    case1 = 0
    if curr_weight + items[i][0] <= weight:
        case1 = items[i][1] + knapsack(items, i+1, curr_weight+items[i][0], weight, dp)
    
    case2 = knapsack(items, i+1, curr_weight, weight, dp)
    
    dp[i][curr_weight] = max(case1, case2)
    return dp[i][curr_weight]

if __name__ == "__main__":
    items = [(10,60),(20,100),(30,120)]
    w = 50
    dp = [[-1 for _ in range(w+1)] for _ in range(len(items))]  
    print("Maximum profit is:", knapsack(items, 0, 0, w, dp))
