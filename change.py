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


def makechange_bottomup_with_cent(coins, amount):
    """
    Assumes there is a coin worth 1.
    """
    # initialize our countmemo
    count_table = [0] * (amount + 1)

    for i in range(1, amount+1):
        # in the worst case we can get the amount by adding another coin
        count_table[i] = count_table[i-1] + 1
        # look at larger coins that are less than our amount to find any better solution
        for coin in coins:

            if coin <= i:
                result = count_table[i-coin]

            if result < count_table[i]:
                count_table[i] = result + 1

    return count_table[amount]


def makechange_bottomup(coins, amount):
    # setting array elements to some large value that is not possible answer
    min_count_table = [amount + 1] * (amount + 1)

    min_count_table[0] = 0  # setting the base case

    for i in range(1, amount + 1):  # iterate through all possible amount values from base case
        for j in range(0, len(coins)):  # find the number of coins needed for each coin denomination
            coin_val = coins[j]
            # if denomination value is less than amount we are seeking (i) then we can use the coin
            if (coin_val <= i):
                # replace min_count_table[i] with minimum value of coins possible
                min_count_table[i] = min(min_count_table[i], min_count_table[i - coin_val] + 1)

    # we have a valid count of coins if min_count_table[amount] is valid
    if min_count_table[amount] > amount:
        result = -1
    else:
        result = min_count_table[amount]

    return result

def makechange_coins(coins, amount):
    """
    Returns the exact coins used for an optimal solution instead of the number of coins used
    """
    # setting array elements to some large value that is not possible answer
    min_count_table = [amount + 1] * (amount + 1)

    # initialize a coin used array that tracks the coin used for each amount
    coin_used = [0] * (amount + 1)

    min_count_table[0] = 0  # setting the base case

    for i in range(1, amount + 1):  # iterate through all possible amount values from base case
        for j in range(0, len(coins)):  # find the number of coins needed for each coin denomination
            coin_val = coins[j]
            # if denomination value is less than amount we are seeking (i) then we can use the coin
            if (coin_val <= i):
                # replace min_count_table[i] with minimum value of coins possible
                if min_count_table[i - coin_val] + 1 < min_count_table[i]:
                    min_count_table[i] = min_count_table[i - coin_val] + 1
                    coin_used[i] = coin_val

    # we have a valid count of coins if min_count_table[amount] is valid (assumes no coin below value 1)
    if min_count_table[amount] > amount:
        return -1

    result = ''
    for x in range(min_count_table[amount]):
        result += '+' + str(coin_used[amount])
        amount -= coin_used[amount]

    return result[1:]





if __name__ == "__main__":
    print(makechange_topdown([1,5,10,25], 180))
    print(makechange_bottomup([1,5,10,25], 180))
    print(makechange_coins([1,5,10,25], 180))



