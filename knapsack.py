# Suppose you woke up on a mysterious island and there are numerous valuable items
# on the island. You have a knapsack (a bag) with you which you can use to take back
# these items with you. But, the problem is there is a limit to the weight that your
# knapsack can carry. So, our questions would be what is the best way to cram items
# into our knapsack to maximize the overall value of items that you can carry back with you.


def unbound_knapsack(W, n, weights, values):
    dp = [0]*(W+1)

    for x in range(1, W+1):

        for i in range(n):
            wi = weights[i]
            if wi <= x:
                dp[x] = max(dp[x] , dp[x-wi] + values[i])

    return dp[W]

if __name__ == "__main__":
    print(unbound_knapsack(10,5,[4,9,3,5,7], [10,25,13,20,8]))