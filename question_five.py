# The first thing I thought was to use binary search. 
# However, considering the constraint of 2 eggs and since we are looking for the worst-case scenario, it would be a terrible method.

# After that, I thought about dropping the egg at intervals of 10, and when the first one breaks, 
# I would iterate through the smaller interval until finding the exact floor. 
# Then I managed to calculate the interval size that would lead to the fewest attempts.

# Still, it seemed like there was room for improvement, so I found the following mathematical expression:

def egg_drop():
    n = 1
    while (n * (n + 1)) / 2 < 100:
        n += 1
    return n

result = egg_drop()
print("Number of attempts:", result)

# I the question was to make a function to find the number of attempts for any floors and eggs i would do a very similar solution as question seven.
