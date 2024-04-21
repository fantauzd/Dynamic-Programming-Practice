# given a list of coin denominations and the needed amount of change,
# return the least possible number of coins

import sys
def makechangeBF(coins, amount):
    """
    Brute Force solution to change problem.
    :param coins: A list of coin denominations like [1, 5, 10, 25]
    :param amount: The amount of change to return
    :return: minimum number of coins
    """
    # base case is when we have no amount left to return
    if(amount == 0): return 0
    result = amount+1 #some arbitary huge number that cannot be the answer
    # for each coin denomination
    for i in range(len(coins)):
        # if that denomination is viable for the amount
        if(coins[i] <= amount):
            # find the minimum number of coins to get that amount by checking the
            # branches for the minimum amount of steps to get each amount after subtracting one coin
            result = min(result, makechangeBF(coins, amount-coins[i]) + 1)
    return result


def makechange(coins, amount, countmemo={}):
    """
    Memoization solution to change problem.
    :param coins: A list of coin denominations like [1, 5, 10, 25]
    :param amount: The amount of change to return
    :return: minimum number of coins
    """
    # base case is when we have no amount left to return
    if(amount == 0): return 0
    result = amount+1 #some arbitary huge number that cannot be the answer
    # if we already know the best solution fpr amount then we save time using the memo
    if amount in countmemo:
        return countmemo[amount]
    else:
    # for each coin denomination
        for i in range(len(coins)):
            # if that denomination is viable for the amount
            if(coins[i] <= amount):
                # find the minimum number of coins to get that amount by checking the
                # branches for the minimum amount of steps to get each amount after subtracting one coin
                result = min(result, makechange(coins, amount-coins[i]) + 1)
                # when a better solution is found we add it to the memo
                if amount not in countmemo or result < countmemo[amount]:
                    countmemo[amount] = result
    return result


def makechange_topdown( coins, amount):
    if amount == 0:
        return 0
    return makechange_topdown_helper(coins, amount, [0] * (amount + 1))


def makechange_topdown_helper( coins, amount, countmemo):
    if (amount < 0):
        return -1

    if (amount == 0):
        return 0

    if (countmemo[amount] != 0):
        return countmemo[amount]

    inf = sys.maxsize
    minimum_coins = sys.maxsize  # set to some maximum value
    for coin in coins:
        temp_coincount = makechange_topdown_helper(coins, amount - coin, countmemo)

        if (temp_coincount >= 0 and temp_coincount < minimum_coins):
            minimum_coins = 1 + temp_coincount

    countmemo[amount] = -1 if (minimum_coins == inf) else minimum_coins  # if we found a new minimum use it

    return countmemo[amount]


def makechange_bottomup(coins, amount):
    # initialize our countmemo
    countmemo = [0] * (amount + 1)

    for i in range(1, amount+1):
        # in the worst case we can get the amount by adding another coin
        countmemo[i] = countmemo[i-1] + 1
        # look at larger coins that are less than our amount to find any better solution
        for coin in coins:

            if coin <= i:
                result = countmemo[i-coin]

            if result < countmemo[i]:
                countmemo[i] = result + 1

    return countmemo[amount]



if __name__ == "__main__":
    print(makechange_topdown([1,3,5], 9))
    print(makechange_bottomup([1,3,5], 9))



