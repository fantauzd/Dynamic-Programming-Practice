# Suppose you woke up on a mysterious island and there are numerous valuable items
# on the island. You have a knapsack (a bag) with you which you can use to take back
# these items with you. But, the problem is there is a limit to the weight that your
# knapsack can carry. So, our questions would be what is the best way to cram items
# into our knapsack to maximize the overall value of items that you can carry back with you.

def unbound_knapsack(W, n, weights, values):
    """
    Solves the unbounded knapsack problem in which there are infine amounts of each item.
    :param W: int, the max weight of the sack
    :param n: int, the number of different items to choose from
    :param weights: an array of weight of each item
    :param values: an array of values of each item, index corresponds to weights array
    :return: the max value that can be fit into the knapsack
    """
    dp = [0]*(W+1)

    for x in range(1, W+1):

        for i in range(n):
            wi = weights[i]
            if wi <= x:
                dp[x] = max(dp[x] , dp[x-wi] + values[i])

    return dp[W]

# The 0-1 knapsack problem is the same as the unbounded knapsack problem but with the
# requirement that we place, at most, one object of a kind into the knapsack.
#Thus, the knapsack cannot contain 2 of the same object.

def bound_knapsack(W, n, weights, values):
    """
    Solves the bounded knapsack problem in which there are only one of each item.
    :param W: int, the max weight of the sack
    :param n: int, the number of different items to choose from
    :param weights: an array of weight of each item
    :param values: an array of values of each item, index corresponds to weights array
    :return: the max value that can be fit into the knapsack
    """
    dp = [[0 for p in range(n)] for q in range(W)]

    for x in range(W):
        for i in range(n):

            wi = weights[i]
            if wi <= x:
                dp[x][i] = max(dp[x][i-1] , dp[x-wi][i-1] + values[i])

    return dp[W-1][n-1]


if __name__ == "__main__":
    print(unbound_knapsack(10,5,[4,9,3,5,7], [10,25,13,20,8]))
    print(bound_knapsack(10, 5, [4, 9, 3, 5, 7], [10, 25, 13, 20, 8]))