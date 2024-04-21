# Use Dynamic programming to solve rod cutting problem

# Given a rod of n meters and a list of prices (price[])
# for different lengths of the rod, a rod of length i
# will have a price of price[i-1]. We want to sell the
# rod and make the maximum possible revenue. We can cut
# the rod into lengths of different sizes before selling.
# The price of each piece will be determined by the list
# of prices provided. What is the optimal amount of revenue
# we can get out of the rod given length, n and prices?

def rodCutting_topdown(n, prices):
    """
    A naive recursive solution to the rod cutting problem.
    :param n: The length of the rod
    :param prices: A list of prices for lengths like [1,5,10]
    :return: The optimal price for the rod after any cuts.
    """
    vals = [0] * n
    return rodCutting_topdown_helper(n, prices, vals)

def rodCutting_topdown_helper(n, prices, vals):
    if n <= 0:
        return 0

    if vals[n-1] != 0:
        return vals[n-1]

    for i in range(1, n+1):
        vals[n-1] = max(vals[n-1], rodCutting_topdown_helper(n-i, prices, vals) + prices[i-1])
    return vals[n-1]

if __name__ == "__main__":
    print(rodCutting_topdown(4, [1,5,8,9,10]))