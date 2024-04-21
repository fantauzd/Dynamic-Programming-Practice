# Use Dynamic programming to solve rod cutting problem

# Given a rod of n meters and a list of prices (price[])
# for different lengths of the rod, a rod of length i
# will have a price of price[i-1]. We want to sell the
# rod and make the maximum possible revenue. We can cut
# the rod into lengths of different sizes before selling.
# The price of each piece will be determined by the list
# of prices provided. What is the optimal amount of revenue
# we can get out of the rod given length, n and prices?

def rodCutting_naive(n, prices):
    """
    A naive recursive solution to the rod cutting problem.
    :param n: The length of the rod
    :param prices: A list of prices for lengths like [1,5,10]
    :return: The optimal price for the rod after any cuts.
    """
    if n == 1:
        return prices[0]
    max_val = 0
    for i in range(1, n+1):
        max_val = max(max_val, rodCutting_naive(n-i, prices) + prices[i-1])
    return max_val

if __name__ == "__main__":
    print(rodCutting_naive(4, [1,5,8,9,10]))