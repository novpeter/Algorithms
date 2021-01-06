def knapSack(capacity, weights, values, count): 
    K = [[0 for x in range(capacity + 1)] for x in range(count + 1)] 
  
    for i in range(count + 1): 
        for w in range(capacity + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif weights[i-1] <= w: 
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[count][capacity] 
  
  
values = [60, 100, 120] 
weights = [10, 20, 30] 
capacity = 50
print(knapSack(capacity, weights, values, len(values))) 