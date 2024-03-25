# To solve this question, i used knapsack algorithm. The complexity iss O(number_carrots_types * capacity)

def knapsack(capacity, weights, values, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i][w - weights[i - 1]] + values[i - 1])

    return dp[n][capacity]

def get_max_value(carrot_types, capacity):
    weights = [carrot['kg'] for carrot in carrot_types]
    values = [carrot['price'] for carrot in carrot_types]
    n = len(weights)
    
    return knapsack(capacity, weights, values, n)

# Given exemple
carrot_types = [{'kg': 5, 'price': 100}, {'kg': 7, 'price': 150}, {'kg': 3, 'price': 70}]
capacity = 36
print(get_max_value(carrot_types, capacity))
